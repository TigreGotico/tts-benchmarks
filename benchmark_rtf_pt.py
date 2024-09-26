import os
import random
import time

from json_database import JsonStorage
from ovos_plugin_manager.utils.tts_cache import hash_sentence
from ovos_tts_plugin_espeakng import EspeakNGTTS
from ovos_tts_plugin_google_tx import GoogleTranslateTTS
from ovos_tts_plugin_matxa_multispeaker_cat import MatxaCatalanTTSPlugin
from ovos_tts_plugin_mimic import MimicTTSPlugin
from ovos_tts_plugin_nos import NosTTSPlugin
from ovos_tts_plugin_pico import PicoTTS
from ovos_tts_plugin_piper import PiperTTSPlugin
from pydub import AudioSegment
from tqdm import tqdm  # Progress bar

db = JsonStorage("benchmark_tts_pt.json")


def get_audio_duration(audio_path: str) -> float:
    """Get the duration of an audio file in seconds."""
    audio = AudioSegment.from_file(audio_path)
    return len(audio) / 1000.0  # Convert milliseconds to seconds


def get_rtf(sentences: list, lang: str, plug, voice: str = None):
    # Calculate RTF - real time factor
    wavs = []
    timing = []
    failed = []

    for s in tqdm(sentences, desc=f"Generating TTS for {plug}/{lang}/{voice}", unit="sentence"):
        wav_path = f"/tmp/{lang}_{hash_sentence(str(voice))}_{hash_sentence(repr(plug))}_{hash_sentence(s)}.{plug.audio_ext}"

        # Measure the synthesis time
        start_time = time.time()
        try:
            plug.get_tts(s, wav_file=wav_path, lang=lang, voice=voice)
        except Exception as e:
            print(f"ERROR with sentence '{s}' : {e}")
            failed.append(s)
            continue
        synth_time = time.time() - start_time

        # Get the duration of the generated audio file
        wav_dur = get_audio_duration(wav_path)

        wavs.append(wav_path)
        timing.append((synth_time, wav_dur))

    # Calculate the total synthesis time and total audio duration
    total_synth_time = sum(t[0] for t in timing)
    total_audio_dur = sum(t[1] for t in timing)

    # Calculate RTF
    rtf = total_synth_time / total_audio_dur if total_audio_dur > 0 else float('inf')

    return rtf, wavs, failed


# Define plugins
PLUGINS = [
    # ("plugin_name", TTS_plugin_instance, voice, langs)
    ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), None, ["pt-pt", "pt-br"]),
    ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), None, ["pt-br", "pt-pt"])
]
random.shuffle(PLUGINS)
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
            sentences_file = f"{lang.split('-')[0]}_sentences.txt"
            if not os.path.isfile(sentences_file):
                print(f"Warning: File '{sentences_file}' not found. Skipping {lang}.")
                continue
        with open(sentences_file) as f:
            sentences = [l for l in f.read().split("\n") if l.strip()]

        db[tts_id]["sentences"] = sentences

        if "rtf" in db[tts_id]:
            continue
        # Calculate RTF and generate audio
        rtf, wavs, failed = get_rtf(sentences=sentences, lang=lang, plug=tts, voice=voice)
        print(f"RTF for {plugin_name} in {lang}: {rtf}")
        print("Generated WAV files:", wavs)
        db[tts_id]["rtf"] = rtf
        db[tts_id]["wavs"] = wavs
        db[tts_id]["failed_synths"] = failed
        db.store()
