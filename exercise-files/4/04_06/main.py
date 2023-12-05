import streamlit as st
import tempfile
import openai
import os
from dotenv import load_dotenv
from handlers import speech_to_text

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App
st.title("Audio transcription")  # Add a title

# Custom style for blue button
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: transparent;
            border: 1px solid #3498db;
            float: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# User input
with st.form("user_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Choose a file")
    submit_button = st.form_submit_button(label="Submit")

# Process the uploaded file

if submit_button and uploaded_file is not None:
    with st.spinner("Transcribing..."):
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=os.path.splitext(uploaded_file.name)[1]
        ) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name
            pass
