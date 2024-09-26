from benchmark_wer import benchmark_wer

if __name__ == "__main__":
    LANG = "gl"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", 'gl-ES-SabelaNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'gl-ES-RoiNeural', [LANG]),
        ("ovos-tts-plugin-nos", "celtia", [LANG]),
        ("ovos-tts-plugin-nos", "sabela", [LANG]),
        ("ovos-tts-plugin-cotovia", "sabela", [LANG]),
        ("ovos-tts-plugin-cotovia", "iago", [LANG])
    ]
    benchmark_wer(LANG, PLUGINS)
