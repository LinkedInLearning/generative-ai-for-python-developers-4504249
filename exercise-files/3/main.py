import openai
from colorama import Fore

# Constants

client = openai.OpenAI()


def generate_chat_completion(user_input):
    print("You typed: " + user_input)


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

    user_input = input(Fore.WHITE + "You: ")

    if user_input.lower() == "x":
        main()
    else:
        generate_chat_completion(user_input)


if __name__ == "__main__":
    # Load the environment variables - set up the OpenAI API client
    main()
