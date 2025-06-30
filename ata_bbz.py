pip install pydub

from pydub import AudioSegment
import math
import os

# Configurações
input_path = "caminho_do_arquivo"
chunk_duration_sec = 1800  # 30 minutos = 1800 segundos
output_base = "partes"

# Carrega o áudio
audio = AudioSegment.from_file(input_path, format="mp4")
total_duration_sec = len(audio) // 1000  # em segundos
num_chunks = math.ceil(total_duration_sec / chunk_duration_sec)

contador = 1

# Criação das partes
for i in range(num_chunks):
    start_sec = i * chunk_duration_sec
    end_sec = min((i + 1) * chunk_duration_sec, total_duration_sec)

    # Gera nome da pasta: exemplo '00m_30m', '30m_60m' ou '120m_12741m'
    folder_name = f"{start_sec // 60:02d}m_{end_sec // 60 if end_sec % 60 == 0 else end_sec}m"
    folder_path = os.path.join(output_base, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Corta o trecho do áudio
    chunk = audio[start_sec * 1000:end_sec * 1000]

    # Exporta o arquivo de áudio na pasta criada
    output_file = os.path.join(folder_path, f"parte_{contador}.mp4")
    chunk.export(output_file, format="mp4")
    contador += 1

    print(f"✅ Criado: {folder_path}/parte.mp4")

print("\n🚀 Divisão concluída!")