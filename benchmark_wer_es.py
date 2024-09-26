from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "es-es"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/es/css10/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'es-ES-AlvaroNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'es-ES-ElviraNeural', [LANG]),
        ("ovos-tts-plugin-pico", None, [LANG]),
        ("ovos-tts-plugin-google-tx", None, [LANG]),
        ("ovos-tts-plugin-cotovia", "sabela", [LANG]),
        ("ovos-tts-plugin-cotovia", "iago", [LANG]),
        ("ovos-tts-plugin-espeak", None, [LANG])
    ]
    benchmark_wer(LANG, PLUGINS)
