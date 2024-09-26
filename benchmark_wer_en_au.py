from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "en-au"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", "en-AU-NatashaNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", None, [LANG])
    ]

    benchmark_wer(LANG, PLUGINS)
