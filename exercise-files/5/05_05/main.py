import openai
import json
from colorama import Fore
from dotenv import load_dotenv
from utils import get_current_weather


load_dotenv()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location", "unit"],
            },
        },
    }
]


# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
messages = [{"role": "system", "content": "You are a helpful assistant"}]

client = openai.OpenAI()


def generate_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    messages.append(
        response.choices[0].message
    )  # extend conversation with assistant's reply
    return response.choices[0].message


available_functions = {
    "get_current_weather": get_current_weather,
}  # only one function in this example, but you can have multiple


def call_function(tool_calls):
    if tool_calls:
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )

            print(function_response)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response


def main():
    print(
        Fore.CYAN
        + "Bot: Hello, I am a helpful assistant. Type 'exit' to quit."
        + Fore.RESET
    )

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            print("Goodbye!")
            break

        # Step 1: send the conversation and available functions to GPT
        message_response = generate_response(user_input)
        print(message_response)

        # Step 2: check if GPT wanted to call a function and generate an extended response
        if message_response.tool_calls is None:
            print("Bot: " + message_response.content)
            continue

        # Step 3: call the function
        call_function(message_response.tool_calls)

        # Step 4: send the info on the function call and function response to GPT
        # extend conversation with assistant's reply
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        print("Bot: " + second_response.choices[0].message.content)


if __name__ == "__main__":
    main()
