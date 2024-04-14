import streamlit as st
from io import BytesIO
from assistant import PetalAssitant
import pandas as pd
import json

import pydeck as pdk

def clinics():

    zip_code = st.session_state.get('zip_code', 'Not specified')

    openai_api_key = st.session_state.openai_api_key
    assistant = assistant = PetalAssitant(openai_api_key)

    response = assistant.get_clinics(zip_code)
    st.write(response)

    res = json.loads(response)

    # Convert dictionary to pandas DataFrame
    clinics_df = pd.DataFrame(res['clinics'])

    # # Display the map
    # st.map(clinics_df)
    # Function to join services into a single string
    clinics_df['services_offered'] = clinics_df['services_offered'].apply(lambda x: ', '.join(x))

    # Set up PyDeck layer for the map
    layer = pdk.Layer(
        'TextLayer',  # Use TextLayer to show text
        clinics_df,
        pickable=True,
        get_position='[lo, lat]',
        get_text='name',  # Clinic name will be shown on the map
        get_size=16,
        get_color=[255, 0, 0],  # RGB color of the text
        get_angle=0,
        # Note that text alignment and anchor are necessary for TextLayer
        get_text_anchor='"middle"',
        get_alignment_baseline='"center"'
    )

    # Define the initial view for the PyDeck map
    view_state = pdk.ViewState(
        latitude=clinics_df['lat'].mean(),
        longitude=clinics_df['lon'].mean(),
        zoom=11,
        pitch=0
    )

    # Render PyDeck map in Streamlit
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            'html': '<b>Name:</b> {name}<br /><b>Services Offered:</b> {services_offered}',
            'style': {
                'color': 'white'
            }
        }
    ))


    