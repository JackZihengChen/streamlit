import streamlit as st
import streamlit.components.v1 as components

"# Inserting simple HTML with CSS stylesheet"
HtmlFile = open("MP0.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code)

"# Inserting an iframe"
components.iframe("https://docs.streamlit.io/en/latest")