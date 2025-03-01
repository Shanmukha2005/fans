import streamlit as st
from streamlit.components.v1 import html

with open("fan.html", "r", encoding="utf-8") as f:
    html_content = f.read()

with open("fan.css", "r", encoding="utf-8") as f:
    css_content = f"<style>{f.read()}</style>"

with open("fan.js", "r", encoding="utf-8") as f:
    js_content = f"<script>{f.read()}</script>"

# Inject CSS and JS into the HTML
html_content = html_content.replace("<!-- CSS will be injected here -->", css_content)
html_content = html_content.replace("<!-- JavaScript will be injected here -->", js_content)


# Render the combined content
st.title("Fan By Shannu")
html(html_content, height=1200)
