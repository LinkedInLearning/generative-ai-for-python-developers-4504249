import openai
import os
import json
import requests
from colorama import Fore
from dotenv import load_dotenv


load_dotenv()

# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
messages = [{"role": "system", "content": "You are a helpful assistant"}]

client = openai.OpenAI()


def generate_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    messages.append(response.choices[0].message)
    return response.choices[0].message


def main():
    print(Fore.CYAN + "Bot: Hello, I am a helpful assistant. Type 'exit' to quit." + Fore.RESET)

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            print("Goodbye!")
            break

        # Step 1: send the conversation and available functions to GPT
        message_response = generate_response(user_input)
        print(Fore.CYAN + "Bot: " + message_response.content + Fore.RESET)

        # Step 2: check if GPT wanted to call a function and generate an extended response

        # Step 3: call the function
        # Step 4: send the info on the function call and function response to GPT
        # extend conversation with assistant's reply


if __name__ == "__main__":
    main()