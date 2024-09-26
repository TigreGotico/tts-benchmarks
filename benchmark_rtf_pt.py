from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS

    # Define plugins
    LANG = "pt-pt"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'pt-PT-DuarteNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'pt-PT-RaquelNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'pt-BR-AntonioNeural', ["pt-br"]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'pt-BR-FranciscaNeural', ["pt-br"]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), None, [LANG, "pt-br"]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), None, ["pt-br", LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
