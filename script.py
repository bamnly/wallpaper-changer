# ========== Download the new-bg ==========
import requests

# URL of the file to download
file_url = "https://raw.githubusercontent.com/bamnly/wallpaper-changer/main/images/new-bg.png"

# Send a GET request to the file URL
response = requests.get(file_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the file
    with open("new-bg.png", "wb") as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download file.")



# ========== Set up the new-bg ==========
import ctypes
import os

def set_wallpaper(image_path):
    # Get path to image
    image_path = os.path.abspath(image_path)
    
    # Define SPI_SETDESKWALLPAPER constant
    SPI_SETDESKWALLPAPER = 20
    
    # Set wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Call the function with the path to the downloaded image
set_wallpaper("new-bg.png")





# ========== Download and launch music ==========

import os
import platform
import pygame
import requests

def play_sound(sound_file):
    if platform.system() == "Windows":
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif platform.system() == "Darwin":
        os.system(f"afplay '{sound_file}'")  # macOS
    elif platform.system() == "Linux":
        os.system(f"aplay {sound_file}")  # Linux
    else:
        print("Unsupported operating system.")

def download_sound(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    sound_file = "tu-tu-tu-du-max-verstappen.mp3"
    url = "https://github.com/bamnly/wallpaper-changer/raw/main/sounds/tu-tu-tu-du-max-verstappen.mp3"

    # Download the sound file if it doesn't exist
    if not os.path.exists(sound_file):
        download_sound(url, sound_file)

    play_sound(sound_file)
