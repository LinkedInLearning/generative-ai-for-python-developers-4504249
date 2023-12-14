import streamlit as st
from handlers import downloadFile, generate_image, get_files

desired_size = (600, 400)

# Streamlit App
st.title("🖼️ Image Generation Gallery ✨")  # Add a title
margin = '<div style="margin: 20px 5px;"></div>'

# User input
with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Type something")
    submit_button = st.form_submit_button(label="Send")

# Press Enter to generate response from chatbot
if submit_button:
    with st.spinner("Generating image..."):
        image = generate_image(user_input)
        st.image(image, use_column_width=True)
        saved_image = downloadFile(user_input, image)
        st.success("Image successfully generated and saved to media folder")


def display_gallery():
    """Display all images in the gallery"""
    pass


if __name__ == "__main__":
    display_gallery()
