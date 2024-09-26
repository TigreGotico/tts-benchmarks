from gather_dataset import gather_dataset


if __name__ == "__main__":
    LANG = "nl-nl"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/nl/css10/vits', [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),

       # ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]
    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
