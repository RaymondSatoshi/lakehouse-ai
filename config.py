import streamlit as st

def init_session():
    st.session_state.setdefault("OPENAI_API_KEY", "")
    st.session_state.setdefault("PINECONE_API_KEY", "")
    st.session_state.setdefault("PINECONE_ENVIRONMENT", "")
    # if "OPENAI_API_KEY" not in st.session_state:
    #     st.session_state["OPENAI_API_KEY"] = ""
    # else:
    #     if not st.session_state["OPENAI_API_KEY"] == "" :
    #         chat = ChatOpenAI(open_api_key=st.session_state["OPENAI_API_KEY"])
    # if "PINECONE_API_KEY" not in st.session_state:
    #     st.session_state["PINECONE_API_KEY"] = ""
    # if "PINECONE_ENVIRONMENT" not in st.session_state:
    #     st.session_state["PINECONE_ENVIRONMENT"] = "" 