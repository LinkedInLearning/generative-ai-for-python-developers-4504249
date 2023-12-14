import os
import whisper
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()


def save_file(text, file_name):
    """Saves content on a file"""
    # Ensure the `files` directory exists
    if not os.path.exists("transcriptions"):
        os.makedirs("transcriptions")

    # Open the file in write mode and write the content
    with open(file_name, "w") as file:
        file.write(text)

    print(f"Content saved to {file_name}")


def speech_to_text(audio_path="media/audio.mp3"):
    try:
        if not os.path.exists(audio_path):
            raise FileNotFoundError("File not found")

        # Initialize the Whisper ASR model

        # Your code to transcribe the audio

        # Extract the transcript text from the result

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
