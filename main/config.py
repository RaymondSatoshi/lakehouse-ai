import os
import streamlit as st

def init():
    st.set_page_config(page_title="Lakehouse-ai", layout="wide")
    st.session_state.setdefault("OPENAI_API_KEY", "")
    st.session_state.setdefault("PINECONE_API_KEY", "")
    st.session_state.setdefault("PINECONE_ENVIRONMENT", "")
    st.session_state.setdefault("MESSAGE", [])