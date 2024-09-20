import os
import threading
from pytube import YouTube

# Progress tracking callback function
def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloading: {percentage:.2f}% complete", end='\r')

# Function to download YouTube video with quality selection
def download_youtube_video(url, folder, quality):
    try:
        yt = YouTube(url.strip(), on_progress_callback=show_progress)
        
        # Filter streams based on user input quality
        video_stream = yt.streams.filter(res=quality, progressive=True, file_extension='mp4').first()
        
        if video_stream is None:
            print(f"Requested quality {quality} not available for {url}. Downloading the highest available resolution.")
            video_stream = yt.streams.get_highest_resolution()
        
        local_filename = os.path.join(folder, f"{yt.title}.mp4")
        video_stream.download(output_path=folder, filename=yt.title)
        print(f"\n{local_filename} downloaded.")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Multithreading function remains the same
def multithreaded_download(urls, folder, quality):
    if not os.path.exists(folder):
        os.makedirs(folder)
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_youtube_video, args=(url, folder, quality))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Get input URLs, folder, and desired quality
urls = input("Enter YouTube URLs (comma-separated): ").split(",")
folder = input("Enter download folder: ")
quality = input("Enter desired video quality (e.g., 720p, 1080p): ")
multithreaded_download(urls, folder, quality)
