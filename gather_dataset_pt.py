from gather_dataset import gather_dataset


if __name__ == "__main__":
    LANG = "pt-pt"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/pt/cv/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'pt-PT-DuarteNeural', [LANG]),
        ("ovos-tts-plugin-edge-tts", 'pt-PT-RaquelNeural', [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),
      #  ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
