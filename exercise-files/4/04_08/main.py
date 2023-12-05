import streamlit as st
import tempfile
import openai
import os
from dotenv import load_dotenv
from utils import speech_to_text, speech_to_translation, save_file

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App
st.title("Audio Transcription and Translation")  # Add a title

# Custom style for blue button
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: transparent;
            border: 1px solid #3498db;  # Corrected color code
            float: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

result = ""
# User input
with st.form("user_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Choose a file")
    action = st.selectbox("Choose Action", ["Transcribe", "Translate"])
    submit_button = st.form_submit_button("Submit")

# Process the uploaded file
if submit_button and uploaded_file is not None:
    with st.spinner("Processing..."):
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=os.path.splitext(uploaded_file.name)[1]
        ) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

            # Check the selected action
            if action == "Translate":
                # Translation functionality
                pass

            elif action == "Transcribe":
                # Transcription functionality
                result = speech_to_text(temp_file_path)

            # Display the result
            if result:
                st.success("File processed successfully!")
                st.markdown(f"blue: `{result}`")
                st.audio(uploaded_file, format="audio/mp3")
