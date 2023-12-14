import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import StrOutputParser

from langchain.embeddings.openai import OpenAIEmbeddings


from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

load_dotenv()

embeddings = OpenAIEmbeddings()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "gpt-3.5-turbo-instruct"

template: str = """/
    You are a customer support Chatbot /
    You assist users with general inquiries/
    and technical issues. You will answer to the {question} only based on
    the knowledge {context} you are trained on /
    if you don't know the answer, you will ask the user to rephrase the question  or
    redirect the user the support@abc-shoes.com  /
    always be friendly and helpful  /
    at the end of the conversation, ask the user if they are satisfied with the answer  /
    if yes, say goodbye and end the conversation  /
    """

str_parser = StrOutputParser()
embeddings = OpenAIEmbeddings()

# basic example of how to get started with the OpenAI Chat models
# The above cell assumes that your OpenAI API key is set in your environment variables.
chatmodel = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message_prompt = HumanMessagePromptTemplate.from_template(
    input_variables=["question", "context"],
    template="{question}",
)
chat_prompt_template = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)


def main():
    user_query = "I want to return a pair of shoes?"

    loader = TextLoader("./docs/faq_abc.txt")
    documents = loader.load()

    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)

    # load documents to the vector store - load it into Chroma
    db = Chroma.from_documents(documents, embeddings)

    # search the database by similarity
    docs = db.similarity_search(user_query)

    # return results
    context = docs[0].page_content

    # LCEL makes it easy to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.
    chain = chat_prompt_template | chatmodel | str_parser
    message = chain.invoke({"question": user_query, "context": context})
    print(message)


if __name__ == "__main__":
    main()
