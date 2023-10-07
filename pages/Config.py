from main import config
from PIL import Image
import streamlit as st

config.init()

st.title("Config")

tab1, tab2 = st.tabs(["DataSource", "ApiKey"])

with tab1:
    image = Image.open("image/localdb.jpg")
    st.image(image)

with tab2:
    openai_api_key = st.text_input("OPENAI_API_KEY", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type="password")
    pinecone_api_key = st.text_input("PINECONE_API_KEY", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type="password")
    pinecone_environment = st.text_input("PINECONE_ENVIRONMENT", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type="password")

    # saved = st.button("save")

    # if saved:
    #     st.session_state["OPENAI_API_KEY"] = openai_api_key
    #     st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    #     st.session_state["PINECONE_ENVIRONMENT"] = pinecone_environment