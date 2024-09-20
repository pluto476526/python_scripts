import yt_dlp

def download_video(url, folder):
    ydl_opts = {
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Save with title
        'format': 'best',  # Download best quality available
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Get input URL and folder
url = input("Enter YouTube URL: ")
folder = input("Enter download folder: ")

# Download video
download_video(url, folder)
