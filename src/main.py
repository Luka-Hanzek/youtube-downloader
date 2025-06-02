from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import argparse


def download_audio(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    
    try:
        stream = sorted(yt.streams.filter(only_audio=True), key=lambda x: x.bitrate)[-1]
    except IndexError:
        return
    
    stream.download()

def download_playlist(url):
    yt = Playlist(url)

    for video in yt.videos:
        
        try:
            stream = sorted(video.streams.filter(only_audio=True), key=lambda x: x.bitrate)[-1]
        except IndexError:
            print(f"{video.watch_url} not downloaded.")
            continue
        stream.download()


parser = argparse.ArgumentParser()
parser.add_argument("--url")
cli_args = parser.parse_args()

if "list=" in cli_args.url:
    download_playlist(cli_args.url)
else:
    download_audio(cli_args.url)