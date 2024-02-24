import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image, ImageDraw, ImageOps
from constant import *

st.set_page_config(layout="wide")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# Note: Make sure to replace "...your application code as previously..." with the actual code sections for loading your Lottie animations and other content.
# Load Lottie animations from URLs for skills
python_lottie_url = "https://lottie.host/491102f6-76e7-4c54-9f63-9a2d74740a74/0hvBOPiOqz.json"
data_lottie_url = "https://lottie.host/78bc20e9-96a5-462f-aef0-fb646e3310a8/KCeCkGva00.json"
tensorflow_lottie_url = "https://lottie.host/869aa6a1-59f0-4678-a597-5d9207105aae/EqhZIgzKDk.json"
database_lottie_url = "https://lottie.host/9996ecd3-c31b-4ab7-976d-5e77e700368b/oDfFmYE7JC.json"
snowflake_lottie_url = "https://lottie.host/c3b02119-7eb6-416f-a5bc-6aef6ed1f6ea/HsHZpQcha2.json"
api_lottie_url = "https://lottie.host/d2bb7ad8-c1fc-4d9c-9c43-07cd0a0f16d2/gV5jFyONbI.json"
sql_lottie_url ="https://lottie.host/243483a7-22d7-40ba-8534-85e68ed2f7fc/pIGSk4MtQc.json"
project_management_url = "https://lottie.host/2b7d7b4a-7354-4752-bb9e-9d2a326443f5/NmNFWsFcJO.json"


python_lottie = load_lottieurl(python_lottie_url)
dataviz_lottie = load_lottieurl(data_lottie_url)
tensorflow_lottie = load_lottieurl(tensorflow_lottie_url)
database_lottie = load_lottieurl(database_lottie_url)
snowflake_lottie = load_lottieurl(snowflake_lottie_url)
api_lottie = load_lottieurl(api_lottie_url)
sql_lottie = load_lottieurl(sql_lottie_url)
project_lottie = load_lottieurl(project_management_url)

# adding a sidebar
st.sidebar.markdown("""
[![GitHub](https://img.icons8.com/ios-glyphs/45/FFFFFF/github.png)](https://github.com/Aditya369-dot)
[![LinkedIn](https://img.icons8.com/ios-glyphs/45/FFFFFF/linkedin-circled--v2.png)](https://www.linkedin.com/in/aditya-b-231a0a194/)
[![Twitter](https://img.icons8.com/ios-glyphs/40/FFFFFF/twitter.png)](https://twitter.com/adibholla21)
[![Instagram](https://img.icons8.com/ios-glyphs/45/FFFFFF/instagram-new.png)](https://www.instagram.com/aditya_4real/?next=%2Foauth%2Foidc%2F%3Fapp_id%3D1289884158313322%26scope%3Dopenid%26response_type%3Dcode%26state%3DATB3TBXUaFJLKVN4dV5PYrDMQbVb4gYfCo_NtC7hKYeXi_xGSJiosSqUdnYymaMoKJCIQ-uoXpCCDDfHA95spC5vL_FHjyYUfkdMmj9igbQgB-ULu0BNLWW_VlXz7cGbGkSqtdg-Hl5PNAFvQ3Q4T4KkG1A%26redirect_uri%3Dhttps%3A%2F%2Fwww.threads.net%2Flogin%2Foidc%2F%26logger_id%3D31423f7a-6b01-4808-91a7-32c2a0b89ead)
""", unsafe_allow_html=True)

import streamlit as st

def gradient(color1, color2, color3, content1, content2):
    # Create an HTML structure with styling for a gradient header
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:75px;border-radius:12%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:#39ff14;font-size:25px;">{content2}</span></h1>',
                unsafe_allow_html=True)
# Layout with responsive design and specific sizes
with st.container():
   colx, colb = st.columns([1.4,5], gap="small")

with colx:
    st.image("final_img.png")

with colb:
    st.title("")
    st.title("")
    st.title("")
    gradient("#833AB4", "#C13584", "#FFFF", "Hi! I am Aditya Bholla 👋", "Your Go-to Data professional.")


with st.container():
    colz,colm =st.columns([4,2])


with colz:
    st.title("🔍 A Little Bit About Me")
    st.markdown("""
        Welcome to my project showcase. As a seasoned Data Professional, my journey in the field is marked by a deep commitment to translating complex data into actionable insights, driving forward business intelligence initiatives with precision and foresight. My technical prowess spans across a broad spectrum of analytics, business intelligence, and visualization platforms, including <span style="color: #39ff14;">Power BI, Tableau, and Oracle BI</span>, all bolstered by robust data analysis capabilities in <span style="color: #39ff14;">SQL and Python</span>. This foundation allows me to leverage advanced machine learning techniques, utilizing libraries such as <span style="color: #39ff14;">TensorFlow and scikit-learn</span>, to inform strategic planning and foster innovative growth strategies.

        My expertise extends further into the realms of cloud technologies, with proficiency in <span style="color: #39ff14;">Oracle ERP Fusion Cloud, Microsoft Azure, and Snowflake</span>, ensuring scalable and efficient data management solutions. This proficiency in cloud infrastructure is pivotal for deploying flexible and resilient data ecosystems that support the dynamic needs of modern businesses.

        A significant portion of my experience involves the intricacies of Data Science and Data Engineering practices. This includes adept knowledge in <span style="color: #39ff14;">ETL processes and creating robust data pipelines using Apache Airflow</span>, essential for streamlining data workflows and enhancing data quality and accessibility. My capabilities are further enriched by an understanding of <span style="color: #39ff14;">Large Language Models (LLMs) like Gemini and LLAMA</span>, which opens new avenues for leveraging natural language processing to extract insights and automate decision-making processes.

        Moreover, my skill set is complemented by a familiarity with web development frameworks such as <span style="color: #39ff14;">Streamlit, Flask, and Django</span>. This knowledge enables me to build interactive, user-friendly applications that make analytical insights accessible to a broader audience, facilitating data-driven decision-making across organizational levels.

        """, unsafe_allow_html=True)

with colm:
    main_page_animation_url = "https://lottie.host/dcad3487-ab37-4b1c-8cae-47d3c88188ea/QCmC5PmaIN.json"
    main_page_animation = load_lottieurl(main_page_animation_url)
    if main_page_animation:
        st_lottie(main_page_animation, height=400, key="main_page")
    else:
        st.error("Error loading main page animation. Please check the URL and try again.")


# Display the Lottie animations for skills
with st.container():
    st.subheader('⚒️ My Skills')

    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:
        if python_lottie:
            st_lottie(python_lottie, height=150, key="python")
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>Python</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("Python Skill Animation Missing")

    with col2:
        if dataviz_lottie:
            st_lottie(dataviz_lottie, height=150, key="mongodb")
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>Tableau and Power-BI</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("MongoDB Skill Animation Missing")

    with col3:
        if tensorflow_lottie:
            st_lottie(tensorflow_lottie, height=150, key="tensorflow")
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>TensorFlow</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("TensorFlow Skill Animation Missing")

    with col4:
        if database_lottie:
            st_lottie(database_lottie, height=150, key="database")
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>ERP cloud</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("Database Skill Animation Missing")

    with col1:
        if snowflake_lottie:
            st_lottie(snowflake_lottie, height=150, key="snowflake")
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>Snowflake</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("Snowflake Animation missing")

    with col2:
        if api_lottie:
            st_lottie(api_lottie, height=150, key='api')
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'> API</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("API Animation Missing")

    with col3:
        if sql_lottie:
            st_lottie(sql_lottie, height=150, key='github')
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:14px;'>SQL</p>",
                        unsafe_allow_html=True)  # Adjust text styling and alignment
        else:
            st.write("Github animation missing")
    with col4:
        if project_lottie:
            st_lottie(project_lottie, height=150, key='Project')
            st.markdown(
                "<p style='text-align:center; color: #FFFFFF; font-size:14px;'>Project Mgmt.(Servicenow,Jira)</p>",
                unsafe_allow_html=True)
        else:
            st.write('Project animation missing')





