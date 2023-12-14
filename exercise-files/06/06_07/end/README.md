## Project : Build a Custom Q&A Chatbot with OpenAI, LangChain, Chroma and Streamlit

....

## 💻 Project Overview

we will build a custom Q&A chatbot using OpenAI, LangChain and Chroma. We will use the OpenAI API to generate answers to questions, LangChain to translate the questions and answers to and from English, and Chroma to convert the text to speech. We will also use the Google Cloud Text-to-Speech API to convert the text to speech.

## 🛠️ Requirements : Installation & Setup

### Python 3.10.0

`brew install pyenv`
`pyenv install 3.10.0`

switch to python 3.10.0

`pyenv local 3.10.0`

### packages

- **LangChain** :[LangChain](https://www.langchain.com/) is a Python library that translates text to and from any language. It uses the Google Translate API to translate text. It also uses the Google Cloud Text-to-Speech API to convert text to speech.
- **Chroma** : [Chroma](https://www.trychroma.com/) is a Python library that converts text to speech. It uses the Google Cloud Text-to-Speech API to convert text to speech.
- **OpenAI** : [OpenAI](https://python.langchain.com/docs/integrations/platforms/openai) is a Python library that provides a simple interface to the OpenAI API. It also provides a command-line interface (CLI) for interacting with the API.
- **python-dotenv** : [python-dotenv](https://pypi.org/project/python-dotenv/) is a Python library that loads environment variables from a .env file. It is used to load the OpenAI API key from the .env file.
- **Streamlit** : [Streamlit](https://streamlit.io/) is a Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. It is used to create the web app.

## 🌐 Create a virtual environment & activate the virtual environment :

**MacOS/Linux**:

```
python3 -m venv env
source env/bin/activate

```

**Windows**:

```
python -m venv env
source env/bin/activate
```

## 🏗️ Installation:

### Install Python 3.6 or higher

use pip3 on a Mac or Linux and pip on Windows

```
pip install -r requirements.txt
pip install --upgrade langchain
```

## [Get an API key](https://platform.openai.com/account/api-keys)

### Set the key as an environment variable:

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

.env file:

```
OPENAI_API_KEY=sk-brHeh...A39v5iXsM2
```

## ▶️ Start the app:

`python main.py`

## ▶️ start streamlit app on localhost:8501:

`streamlit run main.py`
