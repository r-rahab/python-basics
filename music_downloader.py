# yt-dlp
# pip install yt-dlp
# pip install imageio-ffmpeg
import yt_dlp

video_url = "https://www.youtube.com/watch?v=Gr2bA77_m9A"

# Configuration options (mimics command-line flags)
ydl_opts = {
    "format": "bestaudio/best",
    'ffmpeg_location': r'C:\ffmpeg\bin'
    "postprocessors": [0
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",  # You can change to '320' or '0'
        }
    ],
}

# Use a context manager to handle the download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")