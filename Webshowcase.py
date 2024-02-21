import streamlit as st
import requests
from streamlit_lottie import st_lottie


# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Display the title with custom styles
st.title('Hi! I am Aditya Bholla 👋')
st.info("Welcome to my Portfolio ")

# Main page animation
main_page_animation_url = "https://lottie.host/dcad3487-ab37-4b1c-8cae-47d3c88188ea/QCmC5PmaIN.json"
main_page_animation = load_lottieurl(main_page_animation_url)

if main_page_animation:
    st_lottie(main_page_animation, height=300, key="main_page")
else:
    st.error("Error loading main page animation. Please check the URL and try again.")

# Load Lottie animations from URLs for skills
python_lottie_url = "https://lottie.host/491102f6-76e7-4c54-9f63-9a2d74740a74/0hvBOPiOqz.json"
mongodb_lottie_url = "https://lottie.host/085add69-1289-43da-970d-41dd691a4c8a/0hhlo3TVSC.json"
tensorflow_lottie_url = "https://lottie.host/869aa6a1-59f0-4678-a597-5d9207105aae/EqhZIgzKDk.json"
database_lottie_url = "https://lottie.host/9996ecd3-c31b-4ab7-976d-5e77e700368b/oDfFmYE7JC.json"

python_lottie = load_lottieurl(python_lottie_url)
mongodb_lottie = load_lottieurl(mongodb_lottie_url)
tensorflow_lottie = load_lottieurl(tensorflow_lottie_url)
database_lottie = load_lottieurl(database_lottie_url)

# Ensure there's a fallback in case the Lottie animations can't be loaded
if not python_lottie or not mongodb_lottie or not tensorflow_lottie or not database_lottie:
    st.error("Error loading one or more animations. Please check the URLs and try again.")

# Display the Lottie animations for skills
with st.container():
    st.subheader('⚒️ My Skills')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if python_lottie:
            st_lottie(python_lottie, height=150, key="python")
        else:
            st.write("Python Skill Animation Missing")

    with col2:
        if mongodb_lottie:
            st_lottie(mongodb_lottie, height=150, key="mongodb")
        else:
            st.write("MongoDB Skill Animation Missing")

    with col3:
        if tensorflow_lottie:
            st_lottie(tensorflow_lottie, height=150, key="tensorflow")
        else:
            st.write("TensorFlow Skill Animation Missing")

    with col4:
        if database_lottie:
            st_lottie(database_lottie, height=150, key="database")
        else:
            st.write("Database Skill Animation Missing")

# Tableau skill using an image


# You can add additional skills or sections by following the same pattern


# You can add additional skills in the same manner by creating more columns and loading respective Lottie animations




