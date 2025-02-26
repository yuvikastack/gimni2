from dotenv import load_dotenv
load_dotenv() #loading all the enviroment varibles

import streamlit as st # type: ignore
import os
import google.generativeai as genai # type: ignore
from PIL import Image
import io

genai.configure(api_key= os.getenv(" GOOGLE_API_KEY"))

#function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image):
    image_data = None  # Default to None if no image is uploaded

    # Convert image to bytes if uploaded
    if image:
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format="JPEG")
        image_data = {"mime_type": "image/jpeg", "data": img_byte_array.getvalue()}

    # Ensure there's always a text prompt
    if not input_text:
        input_text = "Describe the image."  # ✅ Default text prompt

    # Create input list
    inputs = [input_text]
    if image_data:
        inputs.append(image_data)

    # Generate response
    response = model.generate_content(inputs)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input= st.text_input("Input prompt: ", key="input")

uploaded_file= st.file_uploader("Choose an image....", type=["jpg", "jpeg","png"])
image=None
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## if submit is clicked

if submit:
    response= get_gemini_response(input, image)
    st.subheader("The Reason is")
    st.write(response)