import pytube
link = input ("Pase Youtube video url Here: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Video Has Been Downloaded!")