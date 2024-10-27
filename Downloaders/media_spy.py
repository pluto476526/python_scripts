import requests
from bs4 import BeautifulSoup
import os

def get_video_links(url):
    """Fetches video links, iframe srcs, and <video> sources from the given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    video_links = []

    # Find direct video links
    for a_tag in soup.find_all('a', href=True):
        if a_tag['href'].endswith(('.mp4', '.avi', '.mov', '.wmv')):  # Check for common video file extensions
            full_link = a_tag['href'] if a_tag['href'].startswith('http') else url + a_tag['href']
            video_links.append(full_link)

    # Find iframe srcs
    for iframe in soup.find_all('iframe', src=True):
        iframe_src = iframe['src']
        full_iframe_src = iframe_src if iframe_src.startswith('http') else url + iframe_src
        video_links.append(full_iframe_src)

    # Find <video> tags and their sources
    for video in soup.find_all('video'):
        source_tags = video.find_all('source')
        for source in source_tags:
            if 'src' in source.attrs:
                video_links.append(source['src'])
        
        # If no <source> tags found, check the <video> tag directly
        if not source_tags and 'src' in video.attrs:
            video_links.append(video['src'])

    return video_links

def download_video(video_url):
    """Downloads the video from the given URL."""
    try:
        response = requests.get(video_url, stream=True)
        file_name = os.path.basename(video_url)  # Extracts the file name from the URL
        print(f"Downloading {file_name}...")
        
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*1024):  # Download in chunks of 1MB
                if chunk:
                    f.write(chunk)
        print(f"{file_name} downloaded successfully!")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to check for videos: ")
    
    print("Fetching video links...")
    videos = get_video_links(url)
    
    if videos:
        print("Found video links and sources:")
        for index, link in enumerate(videos):
            print(f"{index + 1}: {link}")
        
        # Prompt user to download all or specific videos
        download_choice = input("Do you want to download all videos? (yes/no): ").strip().lower()
        
        if download_choice == 'yes':
            for link in videos:
                download_video(link)
        else:
            video_choice = int(input("Enter the number of the video to download: ")) - 1
            
            if 0 <= video_choice < len(videos):
                download_video(videos[video_choice])
            else:
                print("Invalid choice.")
    else:
        print("No videos found.")