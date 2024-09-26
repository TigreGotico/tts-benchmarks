from gather_dataset import gather_dataset


if __name__ == "__main__":
    LANG = "ca"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/ca/custom/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'ca-ES-JoanaNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'ca-ES-EnricNeural', [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),

      #  ("ovos-tts-plugin-espeak", "robot", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "central/grau", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "central/elia", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "balear/quim", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "balear/olga", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "valencia/lluc", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "valencia/gina", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "nord-occidental/pere", [LANG]),
        ("ovos-tts-plugin-matxa-multispeaker-cat", "nord-occidental/emma", [LANG]),
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
