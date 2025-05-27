from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

user_input = st.text_input("Enter yout prompt...")

if st.button('Summarize'):
    st.text("Some random text")
