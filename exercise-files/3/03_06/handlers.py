import openai
import os
import json
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
client = openai.OpenAI()

# Constants
API_KEY = os.getenv("OPENAI_API_KEY")  # Get the key from environment variables
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a helpful assistant"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]


def print_messages(messages):
    messages = [
        json.dumps(message) for message in messages if message["role"] != "system"
    ]
    for message in messages:
        m = json.loads(message)
        role = "Bot" if m["role"] == "assistant" else "You"
        print(Fore.BLUE + role + ": " + m["content"])
    return messages


def generate_chat_completion(user_input=""):
    openai.api_key = API_KEY
    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.9,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    if completion:
        message = {
            "role": "assistant",
            "content": completion.choices[0].message.content,
        }
        messages.append(message)
        print_messages(messages)
        return completion.choices[0].message.content.replace("\n", "")
