from benchmark_rtf import benchmark_rtf

if __name__ == "__main__":
    from ovos_tts_plugin_edge_tts import EdgeTTSPlugin
    from ovos_tts_plugin_nos import NosTTSPlugin

    # Define plugins
    LANG = "gl"

    _NOS = NosTTSPlugin(config={})

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'gl-ES-SabelaNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", EdgeTTSPlugin(config={}), 'gl-ES-RoiNeural', [LANG]),
        ("ovos-tts-plugin-nos", _NOS, "celtia", [LANG]),
        ("ovos-tts-plugin-nos", _NOS, "sabela", [LANG]),
        ("ovos-tts-plugin-cotovia", _NOS.cotovia, "sabela", [LANG]),
        ("ovos-tts-plugin-cotovia", _NOS.cotovia, "iago", [LANG])
    ]

    benchmark_rtf(LANG, PLUGINS)
