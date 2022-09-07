import streamlit as st
import streamlit.components.v1 as components

"### Inserting simple HTML with CSS stylesheet"
HtmlFile = open("MP0.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, width=750, height=750, scrolling=True)

"### Inserting an iframe"
components.iframe("https://docs.streamlit.io/en/latest", width=1000, height=500, scrolling=True)

st.snow()

"### Inserting simple HTML with CSS stylesheet"
HtmlFile = open("Okta.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=800)