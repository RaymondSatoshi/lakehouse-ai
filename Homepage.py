import config
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

config.init_session()


if st.session_state["OPENAI_API_KEY"]:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])
else:
    chat = None

st.set_page_config(page_title="Lakehouse-ai", layout="wide")
st.title("TalkWithLakehouse")

# with st.container():
#     st.header("Config")
#     st.markdown(f"""
#         |OpenAI API Key|PINECONE API KEY|PINECONE ENVIRONMENT|
#         |-|-|-|
#         |{st.session_state["OPENAI_API_KEY"]}|{st.session_state["PINECONE_API_KEY"]}|{st.session_state["PINECONE_ENVIRONMENT"]}|
#      """)
    
with st.container():
    # st.header("Chat With Lakehouse")
    if chat:
        question = st.text_input("Question", value="", max_chars=None, key=None, type="default")
        ask = st.button("Ask")
        if ask:
            response = chat([HumanMessage(content=question)])
            st.write(response.content)
    else:
        st.warning("plz set your key in the config page")