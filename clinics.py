import streamlit as st
from io import BytesIO
from assistant import PetalAssitant
import pandas as pd
import json

def clinics():

    zip_code = st.session_state.get('zip_code', 'Not specified')

    openai_api_key = st.session_state.openai_api_key
    assistant = assistant = PetalAssitant(openai_api_key)

    response = assistant.get_clinics(zip_code)
    st.write(response)

    res = json.loads(response)

    # Convert dictionary to pandas DataFrame
    clinics_df = pd.DataFrame(res['clinics'])

    # Display the map
    st.map(clinics_df)


    