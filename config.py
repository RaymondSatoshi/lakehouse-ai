import streamlit as st

def init_session():
    st.session_state.setdefault("OPENAI_API_KEY", "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")
    st.session_state.setdefault("PINECONE_API_KEY", "")
    st.session_state.setdefault("PINECONE_ENVIRONMENT", "")
    st.session_state.setdefault("MESSAGE", [])