import streamlit as st
from googletrans import Translator
st.title("Language Translator")
language_list={"English":"en" ,"Hindi" : "hin" }
col1,col2 = st.columns(2)
with col1:
    selected1=st.selectbox('From',language_list)
    input=st.text_input("Type here")
with col2:
    selected2=st.selectbox('To',language_list)
    translator=Translator()
    translation=translator.translate(input,dest=selected2)
    st.text("Translated text")
    st.text(translation.text)