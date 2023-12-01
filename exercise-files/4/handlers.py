import openai
from dotenv import load_dotenv
import os


load_dotenv()
client = openai.OpenAI()

# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a helpful assistant"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]


def moderate(user_input):
    response = client.moderations.create(input=user_input)
    return response.results[0].flagged


def generate_chat_completion(user_input, messages):
    flagged = moderate(user_input)
    print(f"Flagged: {flagged}")
    if flagged:
        return ":red[Your comment has been flagged as inappropriate.]"
    completion = client.chat.completions.create(
        model=MODEL_ENGINE,
        messages=messages,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return completion.choices[0].message.content
