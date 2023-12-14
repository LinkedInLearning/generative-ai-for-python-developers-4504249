import openai
from PIL import Image
import os
import requests
import ssl
from dotenv import load_dotenv


# Specify the folder path
folder_path = "media"

load_dotenv()
client = openai.OpenAI()


def downloadFile(user_input, url):
    """Download a file from a URL"""
    try:
        # It's recommended to verify SSL certificates
        ssl._create_default_https_context = ssl._create_unverified_context
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Process the save path
        file_path = os.path.join(
            "media", os.path.basename("image_" + user_input.replace(" ", "_")) + ".png"
        )

        with open(file_path, "wb") as f:
            f.write(r.content)
        return f"File downloaded successfully and saved to {file_path}"

    except requests.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")


def get_files():
    """Get all image files in the folder"""
    # List all files in the folder
    files = os.listdir(folder_path)
    images = []
    # Filter out image files (assuming JPEG and PNG formats)
    image_files = [f for f in files if f.endswith(".jpg") or f.endswith(".png")]

    # Display each image
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        images.append({"file": image, "title": image_file})
    return images


def generate_image(user_input="a white siamese cat"):
    """Generate an image based on the user input"""
    pass
