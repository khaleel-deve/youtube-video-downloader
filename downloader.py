import yt_dlp

def Download(media_type, link, save_path):
    if media_type.lower() == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best audio available
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save files in the specified folder
            'postprocessors': [{  # Extract audio using ffmpeg or avconv
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Convert to mp3
                'preferredquality': '192',  # Set the quality of audio
            }],
        }
    elif media_type.lower() == 'video':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Download the best video and audio available in mp4
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save files in the specified folder
        }
    else:
        print("Invalid media type specified. Please choose 'audio' or 'video'.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"{media_type.capitalize()} download is completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")

# Get user input
media_type = input("What would you like to download? ('audio' or 'video'): ").strip()
link = input("Enter the YouTube link (video or playlist): ").strip()
save_path = input("Enter the path where you want to save the file(s): ").strip()

# Download based on user input
Download(media_type, link, save_path)
