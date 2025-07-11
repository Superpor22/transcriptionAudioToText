# Transcriptor de Audio a Texto con Python

Este script permite transcribir archivos de audio en formato WAV a texto, utilizando reconocimiento de voz de Google. El audio se divide en fragmentos basados en silencios para mejorar la precisión del reconocimiento.

## 📌 Características

- Divide el audio en fragmentos automáticamente utilizando los silencios.
- Utiliza la API de Google Speech Recognition para transcribir.
- Guarda el texto completo en un archivo `.txt`.
- Soporta audios largos gracias a la división por silencios.

## 🧰 Requisitos

Antes de ejecutar el script, asegúrate de instalar las siguientes dependencias:

```bash
pip install SpeechRecognition pydub
```

Además, asegúrate de tener instalado `ffmpeg`, ya que `pydub` lo necesita para manejar archivos de audio:

- [Descargar FFMPEG](https://ffmpeg.org/download.html)
- Agrega `ffmpeg` al `PATH` de tu sistema.

## 📁 Estructura del Proyecto

```
transcriptor_audio/
│
├── transcribe.py               # Script principal
├── transcripcion.txt           # Archivo generado con la transcripción
└── audio/                      # Carpeta con los fragmentos de audio temporales
```

## ▶️ Uso

1. Asegúrate de que tu archivo de audio esté en formato `.wav`.
2. Modifica la variable `audio_path` en el script con la ruta de tu archivo de audio.
3. Ejecuta el script:

```bash
python transcribe.py
```

4. La transcripción se mostrará en consola y también se guardará en el archivo `transcripcion.txt`.

## 🛠️ Personalización

Puedes ajustar los siguientes parámetros en la función `split_on_silence` para mejorar los resultados según la calidad del audio:

```python
min_silence_len=500          # Duración mínima de silencio para dividir (ms)
silence_thresh=sound.dBFS-14 # Umbral de silencio (dBFS)
keep_silence=500             # Milisegundos de silencio que se mantienen en los fragmentos
```

## 📌 Notas

- El reconocimiento depende de una conexión a internet activa (se conecta a los servidores de Google).
- Si un fragmento no puede ser reconocido, se omitirá con un mensaje de advertencia.

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y personales. Si lo usas en producción, asegúrate de respetar los Términos de Uso de la API de Google Speech Recognition.
