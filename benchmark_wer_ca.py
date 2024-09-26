import os

from jiwer import wer  # To calculate WER (Word Error Rate)
from json_database import JsonStorage
from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_chromium import ChromiumSTT
from ovos_stt_plugin_fasterwhisper import FasterWhisperSTT
from ovos_tts_plugin_espeakng import EspeakNGTTS
from ovos_tts_plugin_google_tx import GoogleTranslateTTS
from ovos_tts_plugin_matxa_multispeaker_cat import MatxaCatalanTTSPlugin
from ovos_tts_plugin_mimic import MimicTTSPlugin
from ovos_tts_plugin_nos import NosTTSPlugin
from ovos_tts_plugin_pico import PicoTTS
from ovos_tts_plugin_piper import PiperTTSPlugin
from pydub import AudioSegment
from speech_recognition import Recognizer, AudioFile
from tqdm import tqdm  # Progress bar
from ovos_utils.parse import fuzzy_match, MatchStrategy

db = JsonStorage("benchmark_tts_ca.json")
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


def get_audio_duration(audio_path: str) -> float:
    """Get the duration of an audio file in seconds."""
    audio = AudioSegment.from_file(audio_path)
    return len(audio) / 1000.0  # Convert milliseconds to seconds


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
              for t, t2 in zip(sentences, transcripts)])/len(sentences)
    return transcripts, score, score2


def get_markdown_table(LANG_STATS, specs):
    # Generate markdown table based on the results
    table = "## OVOS TTS Plugins Benchmarks\n\n"
    # TODO- update
    table += "| **Lang** | **Plugin** | **Voice** | **RTF (Real Time Factor)** | **WER**  | **DAMERAU LEVENSHTEIN SIMILARITY**  |\n"
    table += "|----------|------------|-----------|----------------------------|------------|----------------------------|\n"

    for lang, stats in LANG_STATS.items():
        for stat in stats:
            table += f"| {lang} | {stat['plugin']} | {stat['voice'] or 'Default'} | {stat['RTF']:.4f} | {stat['WER']:.4f} | {stat['similarity']:.4f}  |\n"

    return table

# Define plugins
PLUGINS = [
    # ("plugin_name", TTS_plugin_instance, voice, langs)
    ("ovos-tts-plugin-google-tx", None, None, ["ca"]),
    ("ovos-tts-plugin-espeak", None, None, ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "central/grau", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "central/elia", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "balear/quim", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "balear/olga", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "valencia/lluc", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "valencia/gina", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "nord-occidental/pere", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", None, "nord-occidental/emma", ["ca"]),
]

# random.shuffle(PLUGINS)
SYSTEM = {"cpu_count": os.cpu_count()}
LANG_STATS = {}

# Iterate over plugins and languages
for plugin_name, _, voice, langs in PLUGINS:
    for lang in langs:

        tts_id = f"{lang}/{plugin_name}/{voice or 'default'}"
        print(f"BENCHMARKING: {tts_id}")
        if tts_id not in db:
            db[tts_id] = {"lang": lang, "plugin": plugin_name, "voice": voice}
        print(db[tts_id])

        if "wer" in db[tts_id]:
            continue  # already calculated
        # Initialize language stats
        if lang not in LANG_STATS:
            LANG_STATS[lang] = []

        # Load sentences for the language
        sentences_file = f"{lang}_sentences.txt"
        if not os.path.isfile(sentences_file):
            print(f"Warning: File '{sentences_file}' not found. Skipping {lang}.")
            continue
        with open(sentences_file) as f:
            sentences = [l for l in f.read().split("\n") if l.strip()]

        db[tts_id]["sentences"] = sentences

        # Calculate STT Agreement Score (WER)
        try:
            transcripts, score, score2 = get_WER(wavs=db[tts_id]["wavs"],
                                         sentences=sentences,
                                         lang=lang)
        except Exception as e:
            print("e")
            continue
        print(f"WER for {plugin_name} in {lang}: {score}")
        print(f"DAMERAU_LEVENSHTEIN_SIMILARITY for {plugin_name} in {lang}: {score2}")
        print("Transcripts:", transcripts)
        db[tts_id]["wer"] = score
        db[tts_id]["similarity"] = score2
        db[tts_id]["transcripts"] = transcripts
        db.store()

        # Store results for the language
        LANG_STATS[lang].append({"RTF": db[tts_id]["rtf"],
                                 "WER": db[tts_id]["wer"],
                                 "similarity": db[tts_id]["similarity"],
                                 "plugin": plugin_name,
                                 "voice": voice})
        db.store()

# Generate markdown table
markdown = get_markdown_table(LANG_STATS, specs=SYSTEM)

# Print markdown output
print(markdown)
