from dotenv import load_dotenv
load_dotenv() #loading all the enviroment varibles

import streamlit as st # type: ignore
import os
import google.generativeai as genai # type: ignore

genai.configure(api_key= os.getenv(" GOOGLE_API_KEY"))

#Function to load gemni model and gemini pro model

model= genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

st.set_page_config(page_title= 'Q&A Demo')

st.header("Gemini LLM Application")

input = st.text_input("Input:" , key="input")
submit= st.button("Ask the question")

#function calling 

if submit:
    response= get_gemini_response(input)
    st.write(response)
