from pytube import YouTube
from sys import argv

#link = argv[1]
link = "https://www.youtube.com/watch?v=W6kxvQYWbG8"
yt = YouTube(link)

print(yt.title)
print(yt.views)

d = yt.streams.get_highest_resolution()
#d.download("c\\Users\\kanna\\Downloads\\ytube_videos\\mov")
d.download("c:\\test\\mov")
print("downloaded successfully")