import speech_recognition as SR
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_large_audio(audio_path, output_file):
    r = SR.Recognizer()

    # Cargar el archivo de audio completo
    sound = AudioSegment.from_wav(audio_path)

    # Dividir el audio en fragmentos usando los silencios
    chunks = split_on_silence(sound, 
        min_silence_len=500,  # Ajusta según sea necesario
        silence_thresh=sound.dBFS - 14,  # Umbral de silencio
        keep_silence=500  # Tiempo que mantiene el silencio entre fragmentos
    )

    full_text = ""

    # Abrir el archivo de salida en modo escritura
    with open(output_file, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            # Guardar cada fragmento como un archivo temporal WAV
            chunk_filename = f"audio\\chunk_{i}.wav"
            chunk.export(chunk_filename, format="wav")

            # Usar el reconocimiento de Google en el fragmento
            with SR.AudioFile(chunk_filename) as source:
                audio = r.listen(source)

                try:
                    # Transcribir el fragmento
                    text = r.recognize_google(audio, language='es-ES')
                    full_text += text + " "
                    print(f"Transcrito chunk {i + 1}/{len(chunks)}: {text}")
                    
                except SR.UnknownValueError:
                    print(f"No se pudo reconocer el chunk {i + 1}.")
                except SR.RequestError as e:
                    print(f"Error en la solicitud de Google Speech Recognition: {e}")
            
        # Escribir el texto transcrito en el archivo de salida
        f.write(full_text)
   
    return full_text

if __name__ == "__main__":
    audio_path = "C:\\Users\\wwwpr\\Downloads\\audio_nodo.wav"  # Ruta del archivo de audio
    output_file = "transcripcion.txt"  # Archivo donde se guardará la transcripción
    print("Espere un momento, el audio se está leyendo...")
    text = transcribe_large_audio(audio_path, output_file)
    print("\nTranscripción completa:")
    print(text)
