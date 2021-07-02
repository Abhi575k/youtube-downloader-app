from pytube import YouTube

link = input("Enter the link:")

try:
	yt = YouTube(link)

except:
	print("Invalid Link")

print("\nTitle: ", yt.title)
print("Length: ", yt.length, "s")

streams_video = yt.streams.filter(progressive=True)
streams_audio = yt.streams.filter(only_audio=True)

print("Video Files: \n")
for stream in streams_video:
    print(stream)

print("Audio Files: \n")
for stream in streams_audio:
    print(stream)

itag = input("Enter the itag of file to be downloaded: ")

ys = yt.streams.get_by_itag(itag)

print("Downloading!!")

try:
    ys.download()
    print("File Successfully Downloaded.")

except:
	print("Some Error")