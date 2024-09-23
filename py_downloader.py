import yt_dlp
import sys

def download_video(url, folder):
    ydl_opts = {
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Save with title
        'format': 'bestvideo[height=720]+bestaudio/best[height=720]',  # Only download 720p quality
        'progress_hooks': [hook],  # Hook for progress updates
        'noplaylist': True,  # Prevent downloading playlists
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def hook(d):
    if d['status'] == 'downloading':
        percentage = d['downloaded_bytes'] / d['total_bytes'] * 100 if d['total_bytes'] else 0
        quality = d.get('format', 'unknown')
        speed = d.get('speed_string', 'N/A')
        eta = d.get('eta', 'N/A')

        # Create a progress bar
        bar_length = 40  # Length of the progress bar
        block = int(round(bar_length * percentage / 100))
        progress_bar = f"[{'#' * block}{'-' * (bar_length - block)}] {percentage:.2f}%"
        
        # Print the progress bar and additional info
        sys.stdout.write(f"\r{progress_bar} | Quality: {quality} | Speed: {speed} | ETA: {eta} seconds")
        sys.stdout.flush()
        
    elif d['status'] == 'finished':
        print(f"\nDownload finished! File saved as: {d['filename']}")

# Get input URL and folder
url = input("Enter YouTube URL: ")
folder = input("Enter download folder: ")

# Download video
download_video(url, folder)