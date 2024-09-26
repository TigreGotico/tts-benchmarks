import os
import random
import time

from jiwer import wer  # To calculate WER (Word Error Rate)
from json_database import JsonStorage
from ovos_plugin_manager.templates.stt import STT
from ovos_plugin_manager.utils.tts_cache import hash_sentence
from ovos_stt_plugin_chromium import ChromiumSTT
from ovos_stt_plugin_fasterwhisper import FasterWhisperSTT
from ovos_tts_plugin_matxa_multispeaker_cat import MatxaCatalanTTSPlugin
from ovos_tts_plugin_mimic import MimicTTSPlugin
from ovos_tts_plugin_pico import PicoTTS
from ovos_tts_plugin_nos import NosTTSPlugin
from ovos_tts_plugin_espeakng import EspeakNGTTS
from ovos_tts_plugin_piper import PiperTTSPlugin
from ovos_tts_plugin_cotovia import CotoviaTTSPlugin
from ovos_tts_plugin_google_tx import GoogleTranslateTTS
from pydub import AudioSegment
from speech_recognition import Recognizer, AudioFile
from tqdm import tqdm  # Progress bar

db = JsonStorage("benchmark_tts.json")
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
    return transcripts, score


def get_markdown_table(LANG_STATS, specs):
    # Generate markdown table based on the results
    table = "## OVOS TTS Plugins Benchmarks\n\n"
    # TODO- update
    table += "| **Lang** | **Plugin** | **Voice** | **RTF (Real Time Factor)** | **WER (STT Agreement Score)**  |\n"
    table += "|----------|------------|-----------|----------------------------|----------------------------------------|\n"

    for lang, stats in LANG_STATS.items():
        for stat in stats:
            table += f"| {lang} | {stat['plugin']} | {stat['voice'] or 'Default'} | {stat['RTF']:.4f} | {stat['WER']:.4f}  |\n"

    return table


_NOS = NosTTSPlugin(config={})
_MATXA = MatxaCatalanTTSPlugin(config={})
_PIPER = PiperTTSPlugin(config={})

# Define plugins
PLUGINS = [
    # ("plugin_name", TTS_plugin_instance, voice, langs)
    #("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), None, ["en", "es", "de", "fr", "it", "ca", "nl", "pt", "eu"]),
    ("ovos-tts-plugin-pico", PicoTTS(config={}), None, ["en", "de", "fr", "it"]),
    ("ovos-tts-plugin-nos", _NOS, "celtia", ["gl"]),
    ("ovos-tts-plugin-nos", _NOS, "sabela", ["gl"]),
    #("ovos-tts-plugin-piper", _PIPER, "tugao-medium", ["pt"]),
    ("ovos-tts-plugin-piper", _PIPER, "alan-low", ["en"]),
    #("ovos-tts-plugin-piper", _PIPER, "ryan-low", ["en"]),
    #("ovos-tts-plugin-piper", _PIPER, "ryan-medium", ["en"]),
    #("ovos-tts-plugin-piper", _PIPER, "ryan-high", ["en"]),
    ("ovos-tts-plugin-piper", _PIPER, "carlfm-x-low", ["es"]),
    ("ovos-tts-plugin-cotovia", _NOS.cotovia, "sabela", ["gl", "es"]),
    ("ovos-tts-plugin-cotovia", _NOS.cotovia, "iago", ["gl", "es"]),
    ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), None, ["en", "es", "de", "fr", "it", "ca", "nl", "pt", "eu"]),
    ("ovos-tts-plugin-mimic", MimicTTSPlugin(config={}), "ap", ["en"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "central/grau", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "central/elia", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "balear/quim", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "balear/olga", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "valencia/lluc", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "valencia/gina", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "nord-occidental/pere", ["ca"]),
    ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "nord-occidental/emma", ["ca"]),
]
#random.shuffle(PLUGINS)
SYSTEM = {"cpu_count": os.cpu_count()}
LANG_STATS = {}

# Iterate over plugins and languages
for plugin_name, tts, voice, langs in PLUGINS:
    for lang in langs:

        tts_id = f"{lang}/{plugin_name}/{voice or 'default'}"
        print(f"BENCHMARKING: {tts_id}")
        if tts_id not in db:
            db[tts_id] = {"lang": lang, "plugin": plugin_name, "voice": voice}
        print(db[tts_id])

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
            transcripts, score = get_WER(wavs=db[tts_id]["wavs"],
                                         sentences=sentences,
                                         lang=lang)
        except:
            continue
        print(f"WER for {plugin_name} in {lang}: {score}")
        print("Transcripts:", transcripts)
        db[tts_id]["wer"] = score
        db[tts_id]["transcripts"] = transcripts
        db.store()

        # Store results for the language
        LANG_STATS[lang].append({"RTF": db[tts_id]["rtf"],
                                 "WER": db[tts_id]["wer"],
                                 "plugin": plugin_name,
                                 "voice": voice})
        db.store()

# Generate markdown table
markdown = get_markdown_table(LANG_STATS, specs=SYSTEM)

# Print markdown output
print(markdown)
