import streamlit as st
from langchain_openai import OpenAI

st.title("Simple LLM-App 🤖")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    # Initializing the OpenAI language model with a specified temperature and API key
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "")

    submitted = st.form_submit_button("Submit")

    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")

    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
