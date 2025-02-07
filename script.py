from pytubefix import YouTube

# Definindo pasta de destino
destino = "downloads"

video_url = input("Digite a url do vídeo: ")

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download(output_path=destino)

print(f"Download completo! O vídeo foi salvo em {destino}")
