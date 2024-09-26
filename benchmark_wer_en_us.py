from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "en-us"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/en/vctk/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", "en-US-AriaNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),
        ("ovos-tts-plugin-pico", "pico", [LANG]),
        ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]
    benchmark_wer(LANG, PLUGINS)
