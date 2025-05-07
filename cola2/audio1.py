import speech_recognition as sr

def transcribe_audio():
    reconocedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental...")
        reconocedor.adjust_for_ambient_noise(source, duration=5)

        print("Habla: ")

        try:
            audio = reconocedor.listen(source, timeout=5, phrase_time_limit=20)
            print("Reconociendo...")

            texto = reconocedor.recognize_google(audio, language='es-ES')
            print("Texto reconocido:")
            print(texto)
            return texto
        
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado. No se detectó audio.")
            return None
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento de voz: {e}")
            return None
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return None

if __name__ == "__main__":
    texto = transcribe_audio()
    if texto:
        print("Transcripción completa.")
        print(texto)
    else:
        print("No se pudo transcribir el audio.")