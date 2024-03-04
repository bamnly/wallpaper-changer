# Download the new-bg
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





# Set up the new-bg
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
