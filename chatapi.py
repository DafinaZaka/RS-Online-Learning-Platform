import streamlit as st
import openai
import os 

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    with open(dotenv_path) as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def generate_recommendation(keyword):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I am looking for online courses about '{keyword}'. Can you recommend any?",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        top_p=1.0
    )
    if response and response.choices:
        recommendation = response.choices[0].text.strip()
        return recommendation
    else:
        return ""

st.header('Online Learning Platforms Recommender System')

selected_course = st.text_input("Please give some information about the course you are looking for:")

if selected_course:
    recommendation = generate_recommendation(selected_course)
    if recommendation:
        st.write("Recommended Course:")
        st.write(recommendation)
    else:
        st.write("No recommendation found.")
