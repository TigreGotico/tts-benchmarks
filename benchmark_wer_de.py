from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "de-de"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/de/thorsten/vits', [LANG]),
        ("ovos-tts-plugin-coqui", 'tts_models/de/thorsten/vits--neon', [LANG]),
        ("ovos-tts-plugin-pico", None, [LANG]),
        ("ovos-tts-plugin-google-tx", None, [LANG]),
        ("ovos-tts-plugin-espeak", None, [LANG])
    ]

    benchmark_wer(LANG, PLUGINS)
