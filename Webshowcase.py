import streamlit as st

# Define the CSS code to style the title
title_style = """
<style>
.title-wrapper {
    background-color: rgba(0, 0, 0, 0.5); /* Transparent background */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: #ffffff; /* Text color */
    font-size: 3em; /* Adjust the font size */
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(title_style, unsafe_allow_html=True)

# Display the styled and animated title
st.markdown('<div class="title-wrapper">'
            '<h1>👋 HI! I am Aditya Bholla</h1>'
            '</div>', unsafe_allow_html=True)



# Define the CSS code to set the background image and change text color
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?q=80&w=1720&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed; 
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    font-family: 'Roboto', sans-serif; /* Use Roboto font */
}

</style>
"""


# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Define CSS animation for floating elements with a cooler motion
st.title("")
st.title("")
st.title("")


floating_animation = """
<style>
@keyframes float {
    0% { transform: translateY(0) rotate(0) scale(1); }
    50% { transform: translateY(-20px) rotate(5deg) scale(1.1); }
    100% { transform: translateY(0) rotate(0) scale(1); }
}

.floating-element {
    animation: float 5s ease-in-out infinite;
    position: absolute;
    width: 100px; /* Adjust the size of the symbols */
    height: 100px;
}

.python-symbol {
    top: 20%;
    left: 10%;
}

.sql-symbol {
    top: 200; /* Same top value as Python symbol to align in the same row */
    left: 30%; /* Adjust left value to position next to Python symbol */
}

.ai-symbol {
    top: 400%; /* Same top value as Python symbol to align in the same row */
    left: 50%; /* Adjust left value to position next to SQL symbol */
}

.pie-chart {
    top: 20%; /* Same top value as Python symbol to align in the same row */
    left: 70%; /* Adjust left value to position next to AI symbol */
}
.power-bi-symbol {
    top:400%;
    left:90%;
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(floating_animation, unsafe_allow_html=True)

# Add floating elements (Icons8 icons with HTML code, SQL, AI symbols, and a floating pie chart)

# Inject the CSS into the Streamlit app


# Add floating elements (Icons8 icons with HTML code, SQL, AI symbols, and a floating pie chart)


# Add floating elements (Icons8 icons with HTML code, SQL, AI symbols, and a floating pie chart)


# Create two columns for the floating elements


# Define the floating elements for the first column (Python, SQL, Power BI)



# Inject the CSS into the Streamlit app


# Define CSS code for styling the title and animation


# Display the styled and animated title
st.markdown("<h1 class='SKILLS'> !!</h1>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 =st.columns([1,1,1,1,1])
# Add floating elements (Icons8 icons with HTML code, SQL, AI symbols, and a floating pie chart)
with col1:
    st.markdown('<div class="floating-element python-symbol"><img src="https://img.icons8.com/color/100/000000/python.png" alt="Python Logo"></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="floating-element ai-symbol"><img src="https://img.icons8.com/color/100/000000/artificial-intelligence.png" alt="AI Icon"></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="floating-element power-bi-symbol"><img src="https://img.icons8.com/color/100/000000/power-bi.png" alt="Power BI Icon"></div>', unsafe_allow_html=True)


# Create hero wrapper for your information

col2 = st.sidebar

# Add GitHub, LinkedIn, and Twitter links to column 2
col2.markdown("[![GitHub](https://img.icons8.com/ios-glyphs/45/FFFFFF/github.png)](https://github.com/Aditya369-dot)     "
              "[![LinkedIn](https://img.icons8.com/ios-glyphs/45/FFFFFF/linkedin-circled--v2.png)](https://www.linkedin.com/in/aditya-b-231a0a194/)     "
              "[![Twitter](https://img.icons8.com/ios-glyphs/40/FFFFFF/twitter.png)](https://twitter.com/adibholla21)")









