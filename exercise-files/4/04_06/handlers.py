import os
import whisper
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()


def speech_to_text(audio_path="media/audio.mp3"):
    try:
        if not os.path.exists(audio_path):
            raise FileNotFoundError("File not found")

        # Initialize the Whisper ASR model
        model = whisper.load_model("base")

        # Your code to transcribe the audio
        result = model.transcribe(audio_path)

        # Extract the transcript text from the result
        return result["text"]

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
