from gather_dataset import gather_dataset


if __name__ == "__main__":
    LANG = "de-de"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/de/thorsten/vits', [LANG]),
        ("ovos-tts-plugin-coqui", 'tts_models/de/thorsten/vits--neon', [LANG]),
        ("ovos-tts-plugin-pico", "pico", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),

       # ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]
    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
