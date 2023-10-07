import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv())

if os.environ["OPENAI_API_KEY"]:
     st.session_state["OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]

def init():
    st.set_page_config(page_title="Lakehouse-ai", layout="wide")
    st.session_state.setdefault("OPENAI_API_KEY", "")
    st.session_state.setdefault("PINECONE_API_KEY", "")
    st.session_state.setdefault("PINECONE_ENVIRONMENT", "")
    st.session_state.setdefault("MESSAGE", [])