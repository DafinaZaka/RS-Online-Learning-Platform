import streamlit as st
import openai

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def generate_recommendation(keyword):
    response = openai.Completion.create(
        engine="davinci-codex",
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

selected_course = st.text_input("Search for a course")

if selected_course:
    recommendation = generate_recommendation(selected_course)
    if recommendation:
        st.write("Recommended Course:")
        st.write(recommendation)
    else:
        st.write("No recommendation found.")
