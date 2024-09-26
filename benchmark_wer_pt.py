import os

import librosa
import numpy as np
from jiwer import wer  # To calculate WER (Word Error Rate)
from json_database import JsonStorage
from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_chromium import ChromiumSTT
from ovos_stt_plugin_fasterwhisper import FasterWhisperSTT
from ovos_utils.parse import fuzzy_match, MatchStrategy
from pydub import AudioSegment
from speech_recognition import Recognizer, AudioFile
from tqdm import tqdm  # Progress bar

db = JsonStorage("benchmark_tts_pt.json")
cache = JsonStorage("stt_cache.json")

# Initialize STT
# stt: STT = OVOSHTTPServerSTT({})
stt = ChromiumSTT({})
stt2: STT = FasterWhisperSTT({"model": "large-v3",
                              # "use_cuda": True,
                              # "compute_type": "float16",
                              "beam_size": 5,
                              "cpu_threads": 12
                              })


def analyze_prosody(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Extract pitch (f0) using librosa's pyin algorithm (fundamental frequency)
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

    # Extract duration-based features
    total_duration = librosa.get_duration(y=y, sr=sr)

    # Calculate average pitch variability (standard deviation of f0)
    pitch_variability = np.std(f0[voiced_flag]) if np.any(voiced_flag) else 0

    # Measure pauses by detecting silent frames
    silence_threshold = 0.01
    non_silent_frames = np.sum(np.abs(y) > silence_threshold)
    silence_ratio = 1 - (non_silent_frames / len(y))

    return {
        "total_duration_sec": total_duration,
        "pitch_variability": pitch_variability,
        "silence_ratio": silence_ratio
    }


def get_WER(wavs, sentences, lang):
    # STT Agreement Score - WER of STT transcription (google/fasterwhisper large V3)
    transcripts = []
    for wav in tqdm(wavs, desc=f"Transcribing WAVs for {lang}", unit="file"):
        try:
            if wav in cache:
                transcripts.append(cache[wav])
                continue
            if wav.endswith(".mp3"):
                if not os.path.isfile(f"{wav}.wav"):
                    print(f"converting .mp3 to .wav : {wav}")
                    sound = AudioSegment.from_mp3(wav)
                    sound.export(f"{wav}.wav", format="wav")
                wav = f"{wav}.wav"

            with AudioFile(wav) as source:
                rec = Recognizer()
                audio = rec.record(source)
            try:
                transcript = stt.execute(audio, language=lang)
            except:
                transcript = stt2.execute(audio, language=lang)
            transcripts.append(transcript)
            cache[wav] = transcript
            cache.store()
        except Exception as e:
            print(f"Error transcribing {wav}: {e}")
            transcripts.append(None)
    transcripts = [t if t else "NULL" for t in transcripts]
    # Calculate WER (Word Error Rate) using jiwer
    score = wer(sentences, transcripts)
    score2 = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
                  for t, t2 in zip(sentences, transcripts)]) / len(sentences)
    score3 = [analyze_prosody(w)['pitch_variability'] for w in wavs]
    score3 = sum(score3) / len(wavs)

    return transcripts, score, score2, score3


def get_markdown_table(LANG_STATS, specs):
    # Generate markdown table based on the results
    table = "## OVOS TTS Plugins Benchmarks\n\n"
    table += "| **Lang** | **Plugin** | **Voice** | **RTF (Real Time Factor)** | **WER**  | **DAMERAU LEVENSHTEIN SIMILARITY**  | **Pitch Variability**  |\n"
    table += "|----------|------------|-----------|----------------------------|------------|-----------|-----------------|\n"

    for lang, stats in LANG_STATS.items():
        for stat in stats:
            table += f"| {lang} | {stat['plugin']} | {stat['voice'] or 'Default'} | {stat['RTF']:.4f} | {stat['WER']:.4f} | {stat['similarity']:.4f}  |{stat['pitch_variability']:.4f}  |\n"

    return table


# Define plugins
PLUGINS = [
    # ("plugin_name", TTS_plugin_instance, voice, langs)
    ("ovos-tts-plugin-edge-tts", 'pt-PT-DuarteNeural', ["pt-pt"]),
    ("ovos-tts-plugin-edge-tts", 'pt-PT-RaquelNeural', ["pt-pt"]),
    ("ovos-tts-plugin-edge-tts", 'pt-BR-AntonioNeural', ["pt-br"]),
    ("ovos-tts-plugin-edge-tts", 'pt-BR-FranciscaNeural', ["pt-br"]),
    ("ovos-tts-plugin-google-tx", None, ["pt-pt", "pt-br"]),
    ("ovos-tts-plugin-espeak", None, ["pt-pt", "pt-br"])
]

# random.shuffle(PLUGINS)
SYSTEM = {"cpu_count": os.cpu_count()}
LANG_STATS = {}

# Iterate over plugins and languages
for plugin_name, voice, langs in PLUGINS:
    for lang in langs:
        # Initialize language stats
        if lang not in LANG_STATS:
            LANG_STATS[lang] = []

        tts_id = f"{lang}/{plugin_name}/{voice or 'default'}"
        print(f"BENCHMARKING: {tts_id}")
        if tts_id not in db:
            db[tts_id] = {"lang": lang, "plugin": plugin_name, "voice": voice}
        print(db[tts_id])

        if (db[tts_id].get("wer", 1) < 1 and
                "pitch_variability" in db[tts_id] and
                "similarity" in db[tts_id]):
            # Store results for the language
            LANG_STATS[lang].append({"RTF": db[tts_id]["rtf"],
                                     "WER": db[tts_id]["wer"],
                                     "similarity": db[tts_id]["similarity"],
                                     "pitch_variability": db[tts_id]["pitch_variability"],
                                     "plugin": plugin_name,
                                     "voice": voice})
            continue  # already calculated

        # Load sentences for the language
        sentences_file = f"{lang}_sentences.txt"
        if not os.path.isfile(sentences_file):
            sentences_file = f"{lang.split('-')[0]}_sentences.txt"
            if not os.path.isfile(sentences_file):
                print(f"Warning: File '{sentences_file}' not found. Skipping {lang}.")
                continue
        with open(sentences_file) as f:
            sentences = [l for l in f.read().split("\n") if l.strip()]

        db[tts_id]["sentences"] = sentences

        # Calculate STT Agreement Score (WER)
        try:
            transcripts, score, score2, score3 = get_WER(wavs=db[tts_id]["wavs"],
                                                         sentences=sentences,
                                                         lang=lang)
        except Exception as e:
            print("e")
            continue
        print(f"WER for {plugin_name} in {lang}: {score}")
        print(f"DAMERAU_LEVENSHTEIN_SIMILARITY for {plugin_name} in {lang}: {score2}")
        print(f"PITCH_VARIABILITY for {plugin_name} in {lang}: {score3}")
        print("Transcripts:", transcripts)
        db[tts_id]["wer"] = score
        db[tts_id]["similarity"] = score2
        db[tts_id]["pitch_variability"] = score3
        db[tts_id]["transcripts"] = transcripts
        db.store()

        # Store results for the language
        LANG_STATS[lang].append({"RTF": db[tts_id]["rtf"],
                                 "WER": db[tts_id]["wer"],
                                 "similarity": db[tts_id]["similarity"],
                                 "pitch_variability": db[tts_id]["pitch_variability"],
                                 "plugin": plugin_name,
                                 "voice": voice})
        db.store()

# Generate markdown table
markdown = get_markdown_table(LANG_STATS, specs=SYSTEM)

# Print markdown output
print(markdown)
