from pytube import YouTube
import os

def unduh_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        jalur_simpan_default = os.path.join(os.path.expanduser("~"), "Videos")

        jalur_simpan = jalur_simpan_default

        video.download(jalur_simpan)

        print("Video berhasil diunduh!")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    url_video = input("Masukkan URL video YouTube: ")
    unduh_video(url_video)
