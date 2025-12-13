import streamlit as st

# Set the page to wide mode
st.set_page_config(layout="wide")

# Read the index.html file
with open('index.html', 'r') as f:
    html_code = f.read()

# Display the HTML
st.components.v1.html(html_code, height=800, scrolling=True)
