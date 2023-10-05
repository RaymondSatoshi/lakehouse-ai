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

for message in st.session_state["MESSAGE"]:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

if not chat: st.warning("plz set your key in the config page") 

with st.container():
    question = st.chat_input("Type Something...")
    # question = st.text_input("Question", value="", max_chars=None, key=None, type="default")
    # ask = st.button("Ask")
    if question:
        st.session_state["MESSAGE"].append(HumanMessage(content=question))
        response = chat([HumanMessage(content=question)])
        st.session_state["MESSAGE"].append(response)

    for message in st.session_state["MESSAGE"]:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        else:
            with st.chat_message("user"):
                st.markdown(message.content)

### sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )