import pytube

link = "https://youtu.be/mNuhKUOD_A0"
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Download",link)