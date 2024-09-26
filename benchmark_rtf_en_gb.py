from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS
    from ovos_tts_plugin_mimic import MimicTTSPlugin
    from ovos_tts_plugin_SAM import SAMTTS

    # Define plugins
    LANG = "en-gb"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-SAM", SAMTTS(), None, [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), "en-GB-RyanNeural", [LANG]),
        ("ovos-tts-plugin-mimic", MimicTTSPlugin(config={}), "ap", [LANG]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), "google", [LANG]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), "robot", [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
