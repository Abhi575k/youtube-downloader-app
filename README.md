# youtube-downloader-app
In YouTube, some streams listed have both a video codec and audio codec, while others have just video or just audio, this is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH).
 In the context of pytube, the implications are for the highest quality streams; To download DASH files, you now need to download both the audio and video tracks and then post-process them with software like FFmpeg to merge them.

The legacy streams that contain the audio and video in a single file (referred to as “progressive download”) are still available, but only for resolutions 720p and below.
Progressive streams have the video and audio in a single file, but typically do not provide the highest quality mediameanwhile, adaptive streams split the video and audio tracks but can provide much higher quality.
This YouTube Downloader only supports progressive stream download. Downloading video over 720p will not be possible.
