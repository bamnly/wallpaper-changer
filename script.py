import os
import requests
from pathlib import Path
import ctypes
import platform
import pygame

# Function to download and save the file
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# Function to set the wallpaper
def set_wallpaper(image_path):
    image_path = os.path.abspath(image_path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Function to play the sound
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

if __name__ == "__main__":
    # Get the user's Documents directory
    documents_directory = Path.home() / "Documents"

    # Download the image file
    image_url = "https://raw.githubusercontent.com/bamnly/wallpaper-changer/main/images/new-bg.png"
    image_path = documents_directory / "new-bg.png"
    if not image_path.exists():
        download_file(image_url, image_path)

    # Set the wallpaper
    set_wallpaper(image_path)

    # Download and play the sound file
    sound_url = "https://github.com/bamnly/wallpaper-changer/raw/main/sounds/tu-tu-tu-du-max-verstappen.mp3"
    sound_file = documents_directory / "tu-tu-tu-du-max-verstappen.mp3"
    if not sound_file.exists():
        download_file(sound_url, sound_file)
    play_sound(sound_file)
