import os
import shutil

from json_database import JsonStorage
from ovos_plugin_manager.utils.tts_cache import hash_sentence
from tqdm import tqdm  # Progress bar


def get_wavs(sentences: list, lang: str, plug_name, voice: str = None):
    for s in tqdm(sentences, desc=f"Gathering wav files for {plug_name}/{lang}/{voice}", unit="sentence"):
        wav_path = f"/tmp/{lang}_{hash_sentence(str(voice))}_{hash_sentence(plug_name)}_{hash_sentence(s)}.wav"
        if os.path.isfile(wav_path):
            #print("file exists", wav_path)
            yield wav_path
            continue
        else:
            print(f"WARNING: missing file - {wav_path}")
        wav_path = f"/tmp/{lang}_{hash_sentence(str(voice))}_{hash_sentence(plug_name)}_{hash_sentence(s)}.mp3.wav"
        if os.path.isfile(wav_path):
            #print("file exists", wav_path)
            yield wav_path
        else:
            print(f"WARNING: missing file - {wav_path}")


def gather_dataset(lang: str, PLUGINS: list, outfolder:str=None):
    outfolder = outfolder or f"{os.path.dirname(__file__)}/dataset"
    db = JsonStorage(f"{os.path.dirname(__file__)}/benchmark_tts_{lang}.json")

    # Iterate over plugins and languages
    for plugin_name, voice, langs in PLUGINS:
        for lang in langs:

            tts_id = f"{lang}/{plugin_name}/{voice or 'default'}"
            print(f"GATHERING: {tts_id}")
            if tts_id not in db:
                db[tts_id] = {"lang": lang, "plugin": plugin_name, "voice": voice}

            # Load sentences for the language
            sentences_file = f"{lang}_sentences.txt"
            if not os.path.isfile(sentences_file):
                sentences_file = f"{lang.split('-')[0]}_sentences.txt"
                if not os.path.isfile(sentences_file):
                    print(f"Warning: File '{sentences_file}' not found. Skipping {lang}.")
                    continue
            with open(sentences_file) as f:
                sentences = [l for l in f.read().split("\n") if l.strip()]

            db[tts_id]["sentences"] = sentences

            for w in get_wavs(sentences, lang, plugin_name, voice):
                print(lang, plugin_name, voice, w)
                if outfolder:
                    os.makedirs(f"{outfolder}/{lang}", exist_ok=True)
                    shutil.copy(w, f"{outfolder}/{lang}/{os.path.basename(w)}")


