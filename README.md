## OVOS TTS Plugins Benchmarks

## Metrics

- **RTF - Real Time Factor** - real time factor, how many seconds it takes to create 1 second of audio - (*lower is
  better*)
- **WER - Word Error Rate** - this is a proxy for understandability, assuming more understandable speech scores better (
  WER in STT) - (*lower is better*)
- **DAMERAU LEVENSHTEIN SIMILARITY** - this is also a proxy for understandability, assuming more understandable speech
  scores better - (*higher is better*)

> **NOTE**: for STT google is used, and in case of failure Whisper large V3 as fallback

#### English

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|
| en       | ovos-tts-plugin-google-tx | Default   | 0.1026                     | 0.4426  | 0.8359                             |
| en       | ovos-tts-plugin-pico      | Default   | 0.0115                     | 0.2365  | 0.8933                             |
| en       | ovos-tts-plugin-espeak    | Default   | 0.0021                     | 0.5995  | 0.6137                             |
| en       | ovos-tts-plugin-mimic     | ap        | 0.0253                     | 0.6721  | 0.6721                             |

#### Catalan

| **Lang** | **Plugin**                             | **Voice**            | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** |
|----------|----------------------------------------|----------------------|----------------------------|---------|------------------------------------|
| ca       | ovos-tts-plugin-google-tx              | Default              | 0.1045                     | 0.3062  | 0.9311                             |
| ca       | ovos-tts-plugin-espeak                 | Default              | 0.0025                     | 0.5947  | 0.6748                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | central/grau         | 0.0984                     | 0.3414  | 0.9112                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | central/elia         | 0.1005                     | 0.3590  | 0.9048                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | balear/quim          | 0.0843                     | 0.4956  | 0.8401                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | balear/olga          | 0.1146                     | 0.4956  | 0.8305                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | valencia/lluc        | 0.0832                     | 0.3568  | 0.9175                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | valencia/gina        | 0.1000                     | 0.3744  | 0.9059                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | nord-occidental/pere | 0.1036                     | 0.3436  | 0.9082                             |
| ca       | ovos-tts-plugin-matxa-multispeaker-cat | nord-occidental/emma | 0.0824                     | 0.3612  | 0.9079                             |

#### Spanish

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|
| es       | ovos-tts-plugin-pico      | Default   | 0.0202                     | 0.2268  | 0.9546                             |
| es       | ovos-tts-plugin-google-tx | Default   | 0.0971                     | 0.2268  | 0.9541                             |
| es       | ovos-tts-plugin-cotovia   | sabela    | 0.0865                     | 0.2419  | 0.9465                             |
| es       | ovos-tts-plugin-cotovia   | iago      | 0.0294                     | 0.3218  | 0.8972                             |
| es       | ovos-tts-plugin-espeak    | Default   | 0.0036                     | 0.3888  | 0.8137                             |

#### Galician

| **Lang** | **Plugin**              | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** |
|----------|-------------------------|-----------|----------------------------|---------|------------------------------------|
| gl       | ovos-tts-plugin-nos     | celtia    | 0.5774                     | 0.4369  | 0.9008                             |
| gl       | ovos-tts-plugin-nos     | sabela    | 0.3576                     | 0.5327  | 0.8560                             |
| gl       | ovos-tts-plugin-cotovia | sabela    | 0.1199                     | 0.4533  | 0.8926                             |
| gl       | ovos-tts-plugin-cotovia | iago      | 0.0465                     | 0.5491  | 0.7919                             |

#### Portuguese

| **Lang** | **Plugin**                | **Voice** | **RTF (Real Time Factor)** | **WER** | **DAMERAU LEVENSHTEIN SIMILARITY** |
|----------|---------------------------|-----------|----------------------------|---------|------------------------------------|
| pt-pt    | ovos-tts-plugin-google-tx | Default   | 0.1084                     | 0.3100  | 0.9271                             |
| pt-pt    | ovos-tts-plugin-espeak    | Default   | 0.0020                     | 0.5764  | 0.6959                             |
| pt-br    | ovos-tts-plugin-google-tx | Default   | 0.0850                     | 0.2904  | 0.9348                             |
| pt-br    | ovos-tts-plugin-espeak    | Default   | 0.0019                     | 0.4301  | 0.7515                             |

