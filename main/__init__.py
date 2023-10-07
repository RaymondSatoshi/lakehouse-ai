import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv())

if os.environ["OPENAI_API_KEY"]:
     st.session_state["OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]