import os
import speech_recognition as sr
from pydub import AudioSegment

def transcrever_audio(audio_file):
    # Inicializar o reconhecedor de fala
    r = sr.Recognizer()

    # Obter o caminho completo do arquivo de áudio
    audio_path = os.path.join(os.path.dirname(__file__), audio_file)

    # Verificar se o arquivo de áudio existe
    if not os.path.isfile(audio_path):
        return "Arquivo de áudio não encontrado."

    # Definir a duração máxima de cada parte do áudio (em milissegundos)
    max_duration = 300000

    # Dividir o áudio em partes menores
    audio = AudioSegment.from_wav(audio_path)
    audio_duration = len(audio)

    num_parts = int(audio_duration / max_duration) + 1

    transcriptions = []
    for i in range(num_parts):
        start = max_duration * i
        end = min(max_duration * (i + 1), audio_duration)

        audio_part = audio[start:end]
        audio_part.export("audio_part.wav", format="wav")

        with sr.AudioFile("audio_part.wav") as source:
            audio_part_data = r.record(source)

        try:
            # Transcrever cada parte do áudio separadamente
            texto = r.recognize_google(audio_part_data, language='pt-BR')
            transcriptions.append(texto)
        except sr.UnknownValueError:
            return "Não foi possível transcrever o áudio."

    # Combinar as transcrições das partes em um único texto
    texto_transcrito = ' '.join(transcriptions)
    return texto_transcrito

# Arquivo de áudio que você deseja transcrever (deve ser um arquivo de áudio suportado, como .wav)
audio_file = "audio.wav"

# Chamar a função para transcrever o áudio
texto_transcrito = transcrever_audio(audio_file)

# Imprimir o texto transcrito
print(texto_transcrito)
