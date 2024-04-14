import streamlit as st
from io import BytesIO
from assistant import PetalAssitant

def clinics():

    zip_code = st.session_state.get('zip_code', 'Not specified')

    openai_api_key = st.session_state.openai_api_key
    assistant = assistant = PetalAssitant(openai_api_key)

    response = assistant.get_clinics(zip_code)

    st.write(response)