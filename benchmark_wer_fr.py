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


from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "fr-fr"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/fr/css10/vits', [LANG]),
        ("ovos-tts-plugin-pico", "pico", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),
        ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]

    benchmark_wer(LANG, PLUGINS)
