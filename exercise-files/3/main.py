import openai
from dotenv import load_dotenv
from colorama import Fore


# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a helpful assistant"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]

load_dotenv()
client = openai.OpenAI()


def generate_chat_completion(user_input=""):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )


def main():
    while True:
        print("\n")
        print("----------------------------------------\n")
        print(" *** 🤖 WELCOME TO THE AI-CHATBOT *** ")
        print("\n----------------------------------------")
        print("\n================* MENU *================\n")
        print("[1]- Start Chat")
        print("[2]- Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_chat()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice")


def start_chat():
    print("to end chat, type 'x'")
    print("\n")
    print("      NEW CHAT       ")
    print("---------------------")
    generate_chat_completion()

    while True:
        user_input = input(Fore.WHITE + "You: ")

        if user_input.lower() == "x":
            main()
            break
        else:
            pass
            # generate


if __name__ == "__main__":
    main()
