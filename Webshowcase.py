import streamlit as st

# Define the CSS code to set the background image and change text color
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?q=80&w=1720&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
    font-family: 'Roboto', sans-serif; /* Use Roboto font */
}

.title {
    font-size: 3em; /* Adjust the font size */
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Define CSS animation for floating elements with a cooler motion


# Define CSS animation for floating elements with spacing and in one line
floating_animation = """
<style>
@keyframes float {
    0% { transform: translateY(0) rotate(0) scale(1); }
    50% { transform: translateY(-20px) rotate(5deg) scale(1.1); }
    100% { transform: translateY(0) rotate(0) scale(1); }
}

.floating-container {
    display: flex; /* Use flexbox to align elements in one row */
    justify-content: space-around; /* Space out elements evenly */
}

.floating-element {
    animation: float 5s ease-in-out infinite;
    width: 100px; /* Adjust the size of the symbols */
    height: 100px;
}

.python-symbol {
    /* No need for absolute positioning */
}

.sql-symbol {
    /* No need for absolute positioning */
}

.ai-symbol {
    /* No need for absolute positioning */
}

.pie-chart {
    /* No need for absolute positioning */
}
</style>
"""

# Inject the CSS into the Streamlit app





# Define CSS code for styling the title and animation
title_style = """
<style>
@keyframes fade-in {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

.title {
    font-size: 3em; /* Adjust the font size */
    color: #FFFFFF; /* Set the text color */
    text-align: center; /* Center-align the text */
    padding-top: 100px; /* Add padding to the top */
    font-family: 'Montserrat', sans-serif; /* Use Montserrat font */
    animation: fade-in 2s ease-out; /* Apply fade-in animation */
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(title_style, unsafe_allow_html=True)

# Display the styled and animated title
st.markdown("<h1 class='title'>Aditya Bholla Portfolio !!</h1>", unsafe_allow_html=True)



# Display the styled and animated title

# Inject the CSS into the Streamlit app
st.markdown(floating_animation, unsafe_allow_html=True)

# Add floating elements (Icons8 icons with HTML code, SQL, AI symbols, and a floating pie chart)
st.markdown('<div class="floating-container">'
            '<div class="floating-element python-symbol"><img src="https://img.icons8.com/color/100/000000/python.png" alt="Python Logo"></div>'
            '<div class="floating-element sql-symbol"><img src="https://img.icons8.com/color/100/000000/sql.png" alt="SQL Icon"></div>'
            '<div class="floating-element ai-symbol"><img src="https://img.icons8.com/color/100/000000/artificial-intelligence.png" alt="AI Icon"></div>'
            '<div class="floating-element pie-chart"><img src="https://img.icons8.com/color/100/000000/pie-chart.png" alt="Pie Chart Icon"></div>'
            '</div>', unsafe_allow_html=True)

col2 = st.sidebar

# Add GitHub, LinkedIn, and Twitter links to column 2
col2.markdown("[![GitHub](https://img.icons8.com/ios-glyphs/45/FFFFFF/github.png)](https://github.com/Aditya369-dot)     "
              "[![LinkedIn](https://img.icons8.com/ios-glyphs/45/FFFFFF/linkedin-circled--v2.png)](https://www.linkedin.com/in/aditya-b-231a0a194/)     "
              "[![Twitter](https://img.icons8.com/ios-glyphs/40/FFFFFF/twitter.png)](https://twitter.com/adibholla21)")











