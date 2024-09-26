from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS

    # Define plugins
    LANG = "en-au"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), "google", [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), "en-AU-NatashaNeural", [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
