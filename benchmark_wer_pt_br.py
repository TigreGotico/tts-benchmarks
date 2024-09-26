from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "pt-br"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", 'pt-BR-AntonioNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'pt-BR-FranciscaNeural', [LANG]),
        ("ovos-tts-plugin-google-tx", None, [LANG]),
        ("ovos-tts-plugin-espeak", None, [LANG])
    ]

    benchmark_wer(LANG, PLUGINS)
