import openai
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
client = openai.OpenAI()

# Constants
PERSONA = "A skilled stand-up comedian with a quick wit and charismatic presence, known for their clever storytelling and ability to connect with diverse audiences through humor that is both insightful and relatable."
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "A skilled stand-up comedian with a knack for telling funny stories."
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]


def to_dict(obj):
    return {
        "content": obj.content,
        "role": obj.role,
    }


def print_messages(messages):
    messages = [message for message in messages if message["role"] != "system"]
    for message in messages:
        role = "Bot" if message["role"] == "assistant" else "You"
        print(Fore.BLUE + role + ": " + message["role"])
    return messages


def generate_chat_completion(user_input=""):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    print(completion)
