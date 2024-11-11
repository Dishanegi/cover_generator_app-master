import streamlit as st
from main import get_cover_letter
st.title('Cover Letter Generator')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(job_description, cv, openai_api_key):
  output = get_cover_letter(job_description, cv, openai_api_key)
  st.write(output)

with st.form('my_form'):
    text = st.text_area('Enter Job Description')
    files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=False)

    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text, files, openai_api_key)