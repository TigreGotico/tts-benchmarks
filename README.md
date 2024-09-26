## OVOS TTS Plugins Benchmarks

## Metrics

- **RTF - Real Time Factor** - real time factor, how many seconds it takes to create 1 second of audio - (*lower is
  better*)
- **WER - Word Error Rate** - this is a proxy for understandability, assuming more understandable speech scores better
  in STT, correlates to how many words the TTS pronounces wrong - (*lower is better*)
- **DAMERAU LEVENSHTEIN SIMILARITY** - this is also a proxy for understandability, assuming more understandable speech
  scores better - (*higher is better*)
- **Pitch Variability** - Measures the variation in the pitch of the speech. Higher variability can indicate more
  natural, human-like speech, while low variability may suggest robotic or monotone output. (*Higher is better*)

> **NOTE**: for STT google is used, and in case of failure Whisper large V3 as fallback

#### English

| **Lang** | **Plugin**                | **Voice**           | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|---------------------|----------------------------|---------|------------------------------------|-----------------------|
| en-gb    | ovos-tts-plugin-edge-tts  | en-GB-RyanNeural    | 0.2093                     | 0.3981  | 0.8656                             | 29.8690               |
| en-gb    | ovos-tts-plugin-mimic     | ap                  | 0.0225                     | 0.6721  | 0.6721                             | 14.1314               |
| en-us    | ovos-tts-plugin-edge-tts  | en-US-AriaNeural    | 0.1512                     | 0.3934  | 0.8713                             | 39.8255               |
| en-au    | ovos-tts-plugin-edge-tts  | en-AU-NatashaNeural | 0.1316                     | 0.4473  | 0.7974                             | 49.3665               |
| en-ng    | ovos-tts-plugin-edge-tts  | en-NG-AbeoNeural    | 0.1959                     | 0.4941  | 0.7830                             | 22.9295               |
| en       | ovos-tts-plugin-google-tx | Default             | 0.1026                     | 0.4426  | 0.8359                             | 35.6921               |
| en       | ovos-tts-plugin-pico      | Default             | 0.0115                     | 0.2365  | 0.8933                             | 28.1715               |
| en       | ovos-tts-plugin-espeak    | Default             | 0.0021                     | 0.5995  | 0.6137                             | 8.7964                |

#### Catalan

| **Lang** | **Plugin**                             | **Voice**            | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|----------------------------------------|----------------------|----------------------------|---------|------------------------------------|-----------------------|
| ca       | ovos-tts-plugin-edge-tts               | ca-ES-JoanaNeural    | 0.1812                     | 0.2863  | 0.9378                             | 42.6373               |
| ca       | ovos-tts-plugin-edge-tts               | ca-ES-EnricNeural    | 0.1485                     | 0.2775  | 0.9406                             | 26.2174               |
| ca       | ovos-tts-plugin-google-tx              | Default              | 0.1045                     | 0.3062  | 0.9311                             | 34.3610               |
| ca       | ovos-tts-plugin-espeak                 | Default              | 0.0025                     | 0.5947  | 0.6753                             | 9.0775                |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | central/grau         | 0.0984                     | 0.3414  | 0.9112                             | 23.2631               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | central/elia         | 0.1005                     | 0.3590  | 0.9048                             | 26.2063               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | balear/quim          | 0.0843                     | 0.4956  | 0.8401                             | 20.1048               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | balear/olga          | 0.1146                     | 0.4956  | 0.8305                             | 23.7260               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | valencia/lluc        | 0.0832                     | 0.3568  | 0.9175                             | 19.0406               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | valencia/gina        | 0.1000                     | 0.3744  | 0.9059                             | 38.8802               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | nord-occidental/pere | 0.1036                     | 0.3436  | 0.9082                             | 18.7704               |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | nord-occidental/emma | 0.0824                     | 0.3612  | 0.9079                             | 30.6723               |

#### Spanish

| **Lang** | **Plugin**                | **Voice**          | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|--------------------|----------------------------|---------|------------------------------------|-----------------------|
| es       | ovos-tts-plugin-edge-tts  | es-ES-AlvaroNeural | 0.2365                     | 0.2246  | 0.9535                             | 29.0270               |
| es       | ovos-tts-plugin-edge-tts  | es-ES-ElviraNeural | 0.2291                     | 0.2246  | 0.9521                             | 25.4132               |
| es       | ovos-tts-plugin-pico      | Default            | 0.0202                     | 0.2268  | 0.9546                             | 37.7614               |
| es       | ovos-tts-plugin-google-tx | Default            | 0.0971                     | 0.2268  | 0.9541                             | 30.5998               |
| es       | ovos-tts-plugin-cotovia   | sabela             | 0.0865                     | 0.2419  | 0.9465                             | 26.3303               |
| es       | ovos-tts-plugin-cotovia   | iago               | 0.0294                     | 0.3218  | 0.8972                             | 6.9345                |
| es       | ovos-tts-plugin-espeak    | Default            | 0.0036                     | 0.3888  | 0.8137                             | 8.7267                |

#### Galician

| **Lang** | **Plugin**               | **Voice**          | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|--------------------------|--------------------|----------------------------|---------|------------------------------------|-----------------------|
| gl       | ovos-tts-plugin-edge-tts | gl-ES-SabelaNeural | 0.6924                     | 0.3855  | 0.9181                             | 34.8462               |
| gl       | ovos-tts-plugin-edge-tts | gl-ES-RoiNeural    | 0.2306                     | 0.4136  | 0.8939                             | 21.0103               |
| gl       | ovos-tts-plugin-nos      | celtia             | 0.5774                     | 0.4369  | 0.9008                             | 61.3171               |
| gl       | ovos-tts-plugin-nos      | sabela             | 0.3576                     | 0.5327  | 0.8560                             | 19.8559               |
| gl       | ovos-tts-plugin-cotovia  | sabela             | 0.1199                     | 0.4533  | 0.8926                             | 29.6241               |
| gl       | ovos-tts-plugin-cotovia  | iago               | 0.0465                     | 0.5491  | 0.7919                             | 6.6335                |

#### Portuguese

| **Lang** | **Plugin**                | **Voice**             | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|-----------------------|----------------------------|---------|------------------------------------|-----------------------|
| pt-pt    | ovos-tts-plugin-edge-tts  | pt-PT-DuarteNeural    | 0.2512                     | 0.3515  | 0.9019                             | 20.2053               |
| pt-pt    | ovos-tts-plugin-edge-tts  | pt-PT-RaquelNeural    | 0.2342                     | 0.3362  | 0.9194                             | 30.0802               |
| pt-pt    | ovos-tts-plugin-google-tx | Default               | 0.1084                     | 0.3100  | 0.9271                             | 29.7265               |
| pt-pt    | ovos-tts-plugin-espeak    | Default               | 0.0020                     | 0.5764  | 0.6959                             | 6.8524                |
| pt-br    | ovos-tts-plugin-edge-tts  | pt-BR-AntonioNeural   | 0.5301                     | 0.3297  | 0.9179                             | 31.7333               |
| pt-br    | ovos-tts-plugin-edge-tts  | pt-BR-FranciscaNeural | 0.3377                     | 0.3166  | 0.9269                             | 38.6105               |
| pt-br    | ovos-tts-plugin-google-tx | Default               | 0.0850                     | 0.2904  | 0.9348                             | 28.2025               |
| pt-br    | ovos-tts-plugin-espeak    | Default               | 0.0019                     | 0.4301  | 0.7515                             | 8.0846                |

#### French

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|-----------------------|
| fr       | ovos-tts-plugin-pico      | Default   | 0.0132                     | 0.2894  | 0.9090                             | 23.9790               |
| fr       | ovos-tts-plugin-google-tx | Default   | 0.1160                     | 0.2702  | 0.9271                             | 20.5534               |
| fr       | ovos-tts-plugin-espeak    | Default   | 0.0022                     | 0.4000  | 0.7775                             | 8.0871                |

#### Italian

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|-----------------------|
| it       | ovos-tts-plugin-pico      | Default   | 0.0110                     | 0.2595  | 0.9471                             | 31.1569               |
| it       | ovos-tts-plugin-google-tx | Default   | 0.1058                     | 0.2476  | 0.9551                             | 18.5573               |
| it       | ovos-tts-plugin-espeak    | Default   | 0.0021                     | 0.2595  | 0.8885                             | 8.4683                |

#### German

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** | **Pitch Variability** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|-----------------------|
| de       | ovos-tts-plugin-pico      | Default   | 0.0145                     | 0.2871  | 0.9276                             | 31.3136               |
| de       | ovos-tts-plugin-google-tx | Default   | 0.1078                     | 0.2635  | 0.9476                             | 33.7422               |
| de       | ovos-tts-plugin-espeak    | Default   | 0.0020                     | 0.2541  | 0.8319                             | 8.9455                |

