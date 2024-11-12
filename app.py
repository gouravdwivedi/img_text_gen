import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from io import BytesIO
import streamlit as st
from src.utility import *
from src.logger import logging
from  datetime import datetime

        

st.set_page_config(page_title='Agkiya- Text Genrator', layout = 'wide', page_icon = 'AgkiyaLogo.png', initial_sidebar_state = 'auto')
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.write("Upload an image, and the app will extract any text in the image and save it to a text file.")

# File uploader to upload image files
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Open the image
    image = Image.open(uploaded_image)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text from the image
    with st.spinner("Extracting text..."):
        extracted_text = extract_text_from_image(image)
    
    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)
    
    # Input to specify words to remove (comma-separated)
    # words_to_remove_input = st.text_input("Enter words to remove from the extracted text (comma-separated)")

    # Process the word removal if input is provided
    # if words_to_remove_input:
    #     words_to_remove = words_to_remove_input.split(',')
    #     modified_text = remove_words_from_text(extracted_text, words_to_remove)
    #     st.write("Modified Text (after removing specified words):")
    #     st.write(modified_text)
    # else:
    #     modified_text = extracted_text  # If no words are specified, keep the original text

    # Create an in-memory file for download
    #text_bytes_io = BytesIO(modified_text.encode("utf-8"))
    text_bytes_io = BytesIO(extracted_text.encode("utf-8"))
    FILE_NAME=f"Extract_{datetime.now().strftime('%m_%d-%Y_%H_%M_%S')}.txt" 
    # Provide a download button for the modified text
    st.download_button(
        label="Download Text File",
        data=text_bytes_io,
        file_name=FILE_NAME,
        mime="text/plain"
    )