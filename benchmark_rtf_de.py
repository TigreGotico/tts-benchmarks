from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS
    from ovos_tts_plugin_pico import PicoTTS
    from ovos_tts_plugin_coqui import CoquiTTSPlugin

    # Define plugins
    LANG = "de-de"
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", CoquiTTSPlugin(lang=LANG, config={
            "model": 'tts_models/de/thorsten/vits'}), 'tts_models/de/thorsten/vits', [LANG]),
        ("ovos-tts-plugin-coqui", CoquiTTSPlugin(lang=LANG, config={
            "model": 'tts_models/de/thorsten/vits--neon'}), 'tts_models/de/thorsten/vits--neon', [LANG]),
        ("ovos-tts-plugin-pico", PicoTTS(config={}), None, [LANG]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), None, [LANG]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), None, [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
