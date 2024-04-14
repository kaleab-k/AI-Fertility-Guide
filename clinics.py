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

    response ={ 
                    "clinics": [
                        {
                            "name": "Dr. Michael Dimattina, MD",
                            "lat": 38.8831261402867,
                            "lon": -77.10734461236984,
                            "services_offered": ["General Health", "Specialty Care"],
                        },
                        {
                            "name": "Virginia Center for Reproductive Medicine",
                            "lat": 38.94925562982108, 
                            "lon": -77.32806558381132,
                            "services_offered": ["Reproductive Medicine"],
                        },
                        {
                            "name": "Shady Grove Fertility Center in Washington, D.C.",
                            "lat": 38.90334004167951, 
                            "lon": -77.04549237325074,
                            "services_offered": ["Reproductive Medicine"],
                        }
                    ]
                }
                
    # st.write(response)

    res = response #json.loads(response)

    # Convert dictionary to pandas DataFrame
    clinics_df = pd.DataFrame(res['clinics'])

    if len(res['clinics']) < 1:
        # # Display the map
        st.map(clinics_df)
    else:
        # Function to join services into a single string
        clinics_df['services_offered'] = clinics_df['services_offered'].apply(lambda x: ', '.join(x))

        # Set up PyDeck layer for the map
        layer = pdk.Layer(
            'TextLayer',  # Use TextLayer to show text
            clinics_df,
            pickable=True,
            get_position='[lon, lat]',
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


    