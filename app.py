import pickle
import streamlit as st
import pandas as pd
import re
import json

def extract_first_sentences(text):
    # Use regex to split the text into sentences and return the first 5 sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return ' '.join(sentences[:3])


# def recommend(course):
#     index = courses[courses['Name'] == course].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_courses = []
#     for i in distances[1:6]:
#         course_info = courses.iloc[i[0]]
#         recommended_courses.append({
#             'Name': course_info['Name'],
#             'Institution': course_info['Institution'],
#             'Link': course_info['Link'],
#             'Description': course_info['Description']
#         })

#     return recommended_courses




def recommend(course):
    index = courses[courses['Name'] == course].index[0]  # Get the index from courses DataFrame
    distances = sorted(enumerate(similarity.loc[index]), reverse=True, key=lambda x: x[1])
    recommended_courses = []
    for i in distances[1:6]:
        course_info = courses.iloc[i[0]]
        recommended_courses.append({
            'Name': course_info['Name'],
            'Institution': course_info['Institution'],
            'Link': course_info['Link'],
            'Description': course_info['Description']
        })

    return recommended_courses



st.header('Online Learning Platforms Recommender System')
# courses = pickle.load(open('artifacts/final_data.pkl', 'rb'))
# similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
courses = pd.read_csv('artifacts/final_data.csv')

# Load similarity data from the CSV file
similarity = pd.read_csv('artifacts/similarity.csv')


courses_list = pd.Series(courses['Name'].values)

selected_course = st.text_input("Search for a course")

if selected_course:
    filtered_courses = courses_list[courses_list.str.contains(selected_course, case=False)]
else:
    filtered_courses = courses_list
if selected_course:
    selected_filtered_courses = filtered_courses[filtered_courses['Name'] == selected_course]
    if not selected_filtered_courses.empty:
        recommended_courses = recommend(selected_filtered_courses, selected_course)
       
websites_filter = st.selectbox(
    "Filter by website:",
    ["All", "Udacity", "Coursera", "EdX"]
)

difficulty_filter = st.selectbox(
    "Filter by difficulty level:",
    ["All", "Beginner", "Intermediate", "Advanced"]
)

if websites_filter != "All":
    filtered_courses = filtered_courses[courses['Website'].str.contains(websites_filter)]

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

    
    # Display the link and description of the selected course from the dropdown
    selected_course_info = courses[courses['Name'] == selected_course].iloc[0]
    with st.expander(selected_course_info['Name']):
        st.write("**Link:**", selected_course_info['Link'])
        description = extract_first_sentences(selected_course_info['Description'].replace('�', "'"))
        st.write("**Description:**", description)

    if st.button('Show other similar courses'):
        if selected_course in courses_list.values:
            recommended_courses = recommend(selected_course)
            st.write("Recommended Courses:")
            for course in recommended_courses:
                with st.expander(course['Name']):
                    # st.write("**Institution:**", course['Institution'])
                    st.write("**Link:**", course['Link'])
                    first_sentences = extract_first_sentences(course['Description'].replace('�', "'"))
                    st.write("**Description:**", first_sentences)
                   
        else:
            st.write("Invalid course selected.")

