from pytubefix import YouTube, Playlist
import argparse
import os


def download_audio(url):
    youtube = YouTube(url)
    

    audio_streams = youtube.streams.filter(only_audio=True)
    if not audio_streams:
        return
    
    stream = sorted(audio_streams, key=lambda stream: stream.bitrate)[-1]
    stream.download(output_path=args.dest)


def download_playlist_audio(url, skip_existing=True):
    playlist = Playlist(url)

    if skip_existing:
        playlist_dir = os.path.join(args.dest, playlist.title)
        try:
            existing_tracks = set(os.path.basename(p).split('.')[0] for p in os.listdir(playlist_dir))
        except FileNotFoundError:
            existing_tracks = set()

    for video in playlist.videos:
        if skip_existing:
            
            if video.title in existing_tracks:
                print(f"{video.title} already exists.")
                continue

        audio_streams = video.streams.filter(only_audio=True)
        if not audio_streams:
            print(f"{video.watch_url} not downloaded.")
        
        stream = sorted(audio_streams, key=lambda stream: stream.bitrate)[-1]
        stream.download(output_path=os.path.join(args.dest, playlist.title))


parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True)
parser.add_argument("--dest", required=True)
args = parser.parse_args()

if "playlist" in args.url:
    download_playlist_audio(args.url)
else:
    download_audio(args.url)
