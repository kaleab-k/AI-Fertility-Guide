import streamlit as st
from io import BytesIO
from assistant import PetalAssitant
import pandas as pd

def clinics():

    zip_code = st.session_state.get('zip_code', 'Not specified')

    openai_api_key = st.session_state.openai_api_key
    assistant = assistant = PetalAssitant(openai_api_key)

    response = assistant.get_clinics(zip_code)

    # Convert dictionary to pandas DataFrame
    clinics_df = pd.DataFrame(response['clinics'])

    # Rename columns for compatibility with st.map
    clinics_df.rename(columns={'latitude': 'lat', 'longitude': 'lon'}, inplace=True)

    # Display the map
    st.map(clinics_df)


    st.write(response)