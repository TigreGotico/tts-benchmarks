from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS
    from ovos_tts_plugin_pico import PicoTTS

    # Define plugins
    LANG = "en-us"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), "en-US-AriaNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), None, [LANG]),
        ("ovos-tts-plugin-pico", PicoTTS(config={}), None, [LANG]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), None, [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
