from benchmark_rtf import benchmark_rtf


if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_espeakng import EspeakNGTTS
    from ovos_tts_plugin_google_tx import GoogleTranslateTTS
    from ovos_tts_plugin_matxa_multispeaker_cat import MatxaCatalanTTSPlugin
    from ovos_tts_plugin_nos import NosTTSPlugin
    from ovos_tts_plugin_piper import PiperTTSPlugin
    from ovos_tts_plugin_coqui import CoquiTTSPlugin

    LANG = "ca"

    _NOS = NosTTSPlugin(config={})
    _MATXA = MatxaCatalanTTSPlugin(config={})
    _PIPER = PiperTTSPlugin(config={})

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", CoquiTTSPlugin(lang=LANG), 'tts_models/ca/custom/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'ca-ES-JoanaNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'ca-ES-EnricNeural', [LANG]),
        ("ovos-tts-plugin-google-tx", GoogleTranslateTTS(config={}), "google", [LANG]),
        ("ovos-tts-plugin-espeak", EspeakNGTTS(config={}), "robot", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "central/grau", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "central/elia", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "balear/quim", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "balear/olga", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "valencia/lluc", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "valencia/gina", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "nord-occidental/pere", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", _MATXA, "nord-occidental/emma", [LANG]),
    ]
    benchmark_rtf(LANG, PLUGINS)
