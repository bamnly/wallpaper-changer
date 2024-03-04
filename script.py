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
