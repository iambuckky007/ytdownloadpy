from pytube import YouTube

def download_youtube_video(url, output_path=None):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if output_path is None:
            output_path = yt.title + ".mp4"
        stream.download(output_path)
        print("Download successful!")
    except Exception as e:
        print(f"Error occurred: {e}")


video_url = "https://www.youtube.com/watch?v=e-ORhEE9VVg"
download_youtube_video(video_url)
