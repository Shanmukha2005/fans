import streamlit as st
from streamlit.components.v1 import html

# Read and inject CSS/JS into HTML
with open("fan.html", "r") as f:
    html_content = f.read()

with open("fan.css", "r") as f:
    css_content = f"<style>{f.read()}</style>"

with open("fan.js", "r") as f:
    js_content = f"<script>{f.read()}</script>"

html_content = html_content.replace("</body>", f"{js_content}</body>")
html_content = html_content.replace("</head>", f"{css_content}</head>")

# Render the combined content
st.title("Fan By Shannu")
html(html_content, height=1100)
with open("fan.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
