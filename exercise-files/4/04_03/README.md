## Project : Build a AI-powered Image Gallery

....

**openai**: [OpenAI](https://openai.com/): OpenAI library for Python to build applications with GPT-3.
**streamlit**: [Streamlit](https://streamlit.io/): Streamlit is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science.
**streamlit-chat**: [Streamlit Chat](https://pypi.org/project/streamlit-chat/): Streamlit Chat is a Streamlit component that allows you to add a chatbot to your Streamlit app. It uses OpenAI's GPT-3 to generate responses to user input.
**python-dotenv**: [Python Dotenv](https://pypi.org/project/python-dotenv/): Reads the key-value pair from .env file and adds them to environment variable. It is great for managing app settings during development and in production using 12-factor principles.
**pillow**: [Pillow](https://pypi.org/project/Pillow/): Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

Requirements:

## Create a virtual environment :

**MacOS/Linux**:

```
python3 -m venv env
```

**Windows**:

```
python -m venv env
```

## Activate the virtual environment :

```
source env/bin/activate
```

## Installation:

**MacOS/Linux**:

```
pip3 install -r requirements.txt
pip3 install streamlit streamlit-chat
```

**Windows**:

```
pip install -r requirements.txt
pip install streamlit streamlit-chat
```

## [Get an API key](https://platform.openai.com/account/api-keys)

### Set the key as an environment variable:

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

.env file:

```
OPENAI_API_KEY=sk-brHeh...A39v5iXsM2
```

## Start the app:

`streamlit run main.py`
