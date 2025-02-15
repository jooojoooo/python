import os
import ctypes
import requests
from bs4 import BeautifulSoup

def change_wallpaper(image_path):
    # SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def get_apod():
    # Define the base URL
    base_url = "https://apod.nasa.gov/apod/"
    save_folder = "C:\\Users\\lecke\\.vscode\\python\\bg_change\\images\\"

    # Create the folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Fetch the webpage
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <a> tag with the image link
    link = soup.find("a", href=lambda x: x and "image/" in x)

    if link:
        image_href = link["href"]
        image_url = base_url + image_href  # Full URL of the image
        print(image_url)
        image_name = os.path.basename(image_href)  # Extract file name
        image_path = os.path.join(save_folder, image_name)
        if not os.path.isfile(image_path):

            # Download the image
            img_response = requests.get(image_url, stream=True)
            if img_response.status_code == 200:

                with open(image_path, "wb") as img_file:
                    for chunk in img_response.iter_content(1024):
                        img_file.write(chunk)
                print(f"✅ Image downloaded: {image_path}")
                return image_path
            else:
                print("❌ Failed to download the image.")
        else: print("❌ Image already downloaded")
    else:
        print("❌ No matching image link found.")



script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = script_dir.replace("bg_change", "")
  # Get script's directory
image_path = get_apod()

change_wallpaper(image_path)
