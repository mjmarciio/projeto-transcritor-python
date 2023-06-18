import speech_recognition as sr

def transcrever_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return "Não foi possível transcrever o áudio."
    except sr.RequestError:
        return "Não foi possível conectar-se ao serviço de reconhecimento de fala."

# Pega o arquivo de áudio
audio_file = "audio_curto.wav"

# Chama a função para transcrever o áudio
texto_transcrito = transcrever_audio(audio_file)

print(texto_transcrito)
