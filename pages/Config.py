import config
import streamlit as st

config.init()

st.title("Config")

openai_api_key = st.text_input("OPENAI_API_KEY", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type="password")
pinecone_api_key = st.text_input("PINECONE_API_KEY", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type="password")
pinecone_environment = st.text_input("PINECONE_ENVIRONMENT", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type="password")

saved = st.button("save")

if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = pinecone_environment
