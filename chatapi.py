import streamlit as st
import requests

API_KEY = "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"
API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions"

def generate_recommendations(keyword):
    prompt = f"I am looking for online learning platforms that offer courses related to '{keyword}'. Can you recommend any?\n\nCourse recommendations:"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7,
        "top_p": 1.0
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        output = response.json()
        recommendations = output['choices'][0]['text'].split("\n")
        return recommendations
    else:
        return []

st.header('Online Learning Platforms Recommender System')

selected_course = st.text_input("Search for a course")

if st.button('Show other similar courses'):
    if selected_course:
        recommendations = generate_recommendations(selected_course)
        if recommendations:
            st.write("Recommended Courses:")
            for course in recommendations:
                st.write(course)
        else:
            st.write("No recommendations found.")
    else:
        st.write("Please enter a course to generate recommendations.")
