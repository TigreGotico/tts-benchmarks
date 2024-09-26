from gather_dataset import gather_dataset

if __name__ == "__main__":
    LANG = "en-us"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-coqui", 'tts_models/en/vctk/vits', [LANG]),
        ("ovos-tts-plugin-edge-tts", "en-US-AriaNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),
        ("ovos-tts-plugin-pico", "pico", [LANG]),

        #  ("ovos-tts-plugin-espeak", "robot", [LANG])
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")

    LANG = "en-au"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", "en-AU-NatashaNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG])
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")

    LANG = "en-gb"

    # Define plugins
    PLUGINS = [
        # ("plugin_name", TTS_plugin_instance, voice, langs)
        ("ovos-tts-plugin-edge-tts", "en-GB-RyanNeural", [LANG]),
        ("ovos-tts-plugin-google-tx", "google", [LANG]),

        # ("ovos-tts-plugin-espeak", "robot", [LANG]),
        ("ovos-tts-plugin-mimic", "ap", [LANG]),
        # ("ovos-tts-plugin-SAM", None, [LANG]),
    ]

    gather_dataset(LANG, PLUGINS, outfolder="/home/miro/PycharmProjects/tts-bench-dataset/dataset")
