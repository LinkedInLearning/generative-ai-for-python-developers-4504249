import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import StrOutputParser

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "gpt-3.5-turbo-instruct"

system_prompt = "You are a helpful assistant that answers generals inquiries and assist with technical issues"

str_parser = StrOutputParser()

# basic example of how to get started with the OpenAI Chat models
# The above cell assumes that your OpenAI API key is set in your environment variables.
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt)
human_message_prompt = HumanMessagePromptTemplate.from_template("{question}")
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)


def main():
    user_input = "I want to return a pair of shoes"

    # prompt value
    prompt_value = chat_prompt.invoke({"question": user_input})
    print(prompt_value.to_string())

    # model response

    # string output parser

    # LCEL makes it easy to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.


if __name__ == "__main__":
    main()
