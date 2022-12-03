from pytube import YouTube

def mp3_download(link):
    try:
        yt = YouTube("https://youtu.be/" + link)

    except:
        print("Invalid Link")
        return []
    streams_audio = yt.streams.filter(only_audio=True)
    return streams_audio
    # print("Audio Files: \n")
    # for stream in streams_audio:
    #     print(stream)
    # itag = input("Enter the itag of file to be downloaded: ")
    # ys = yt.streams.get_by_itag(itag)
    # print("Downloading!!")
    # try:
    #     ys.download()
    #     print("File Successfully Downloaded.")
    # except:
    #     print("Some Error")