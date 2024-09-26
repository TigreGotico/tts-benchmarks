from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "en-gb"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", "en-GB-RyanNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", None, [LANG]),
        ("ovos-tts-plugin-pico", None, [LANG]),
        ("ovos-tts-plugin-espeak", None, [LANG]),
        ("ovos-tts-plugin-mimic", "ap", [LANG]),
    ]
    benchmark_wer(LANG, PLUGINS)
