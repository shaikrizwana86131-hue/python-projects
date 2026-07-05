import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text")

source = st.selectbox("Source Language", ["en", "te", "hi"])
target = st.selectbox("Target Language", ["en", "te", "hi"])

if st.button("Translate"):
    translated = GoogleTranslator(source=source, target=target).translate(text)
    st.success(translated)