import google.generativeai as genai
import os
import streamlit as st

# Get API from local environment variable
key = os.getenv('GOOGLE_API_KEY')

# Configure the MODEL
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Create a frontend using streamlit
st.title('SIMPLE TEXT GENERATION')
st.header('This is to test gemini model as application')

prompt = st.text_input('Enter your prompt here', max_chars=10000)

# Only generate if user provides input
if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)
else:
    st.write("👉 Please enter a prompt above.")
