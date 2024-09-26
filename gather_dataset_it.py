from gather_dataset import gather_dataset


if __name__ == "__main__":
    LANG = "it-it"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/it/mai_male/vits', [LANG]),
        ("ovos-tts-plugin-coqui", 'tts_models/it/mai_female/vits', [LANG]),
        ("ovos-tts-plugin-coqui", 'tts_models/it/mai_male/glow-tts', [LANG]),
        ("ovos-tts-plugin-coqui", 'tts_models/it/mai_female/glow-tts', [LANG]),
        ("ovos-tts-plugin-pico", "pico", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),

       # ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
