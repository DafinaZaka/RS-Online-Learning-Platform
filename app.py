import pickle
import streamlit as st
import pandas as pd

def recommend(course):
    index = courses[courses['Name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_courses = []
    for i in distances[1:6]:
        course_info = courses.iloc[i[0]]
        recommended_courses.append({
            'Name': course_info['Name'],
            'Link': course_info['Link'],
            'Description': course_info['Description']
        })

    return recommended_courses

st.header('Online Learning Platforms Recommender System')
courses = pickle.load(open('artifacts/final_data.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

courses_list = pd.Series(courses['Name'].values)

selected_course = st.text_input("Search for a course")

if selected_course:
    filtered_courses = courses_list[courses_list.str.contains(selected_course, case=False)]
else:
    filtered_courses = courses_list

websites_filter = st.selectbox(
    "Filter by website:",
    ["All", "Udacity", "Coursera", "EdX"]
)

difficulty_filter = st.selectbox(
    "Filter by difficulty level:",
    ["All", "Beginner", "Intermediate", "Advanced"]
)

if websites_filter != "All":
    filtered_courses = filtered_courses[courses['Websites'].str.contains(websites_filter)]

if len(filtered_courses) > 0 and difficulty_filter != "All":
    filtered_courses = filtered_courses[
        (courses['Difficulty Level'].fillna('').str.contains(difficulty_filter)) |
        (courses['Difficulty Level'].isnull())
    ]

if len(filtered_courses) == 0:
    st.write("No matching courses found.")
else:
    st.markdown(
        """
        <style>
        .stSelectbox {
            margin-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    selected_course = st.selectbox(
        "Select a course from the dropdown",
        filtered_courses
    )

    if st.button('Show other similar courses'):
        if selected_course in courses_list.values:
            recommended_courses = recommend(selected_course)
            st.write("Recommended Courses:")
            for course in recommended_courses:
                with st.expander(course['Name']):
                    st.write("**Link:**", course['Link'])
                    description = course['Description'].replace('�', "'")
                    st.write("**Description:**", description)
        else:
            st.write("Invalid course selected.")
