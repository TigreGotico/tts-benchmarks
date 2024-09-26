from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS
    from ovos_tts_plugin_coqui import CoquiTTSPlugin

    # Define plugins
    LANG = "nl-nl"
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", CoquiTTSPlugin(lang=LANG), 'tts_models/nl/css10/vits', [LANG]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), "google", [LANG]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), "robot", [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
