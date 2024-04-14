import streamlit as st
from streamlit_card import card

def figma_welcome():
    # Main section with user profile and search bar
    # Section headers
    st.header("MOJO Plan")
    st.subheader("Reproductive Health Information Portal")

    # Services Section
    st.markdown("### Our Services")
    st.markdown("Guidance for your entire reproductive health journey.")

    # Use columns for the services section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Reproductive Health Education")
        st.write("We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs.")

    with col2:
        st.markdown("#### Shared Decision-Making")
        st.write("We help you navigate important conversations through the lens of shared decision-making.")

    with col3:
        st.markdown("#### Personalized Recommendations")
        st.write("Based on your profile, we can provide personalized and precision reproductive health recommendations.")

    
def figa_profile():
    # Function to create a single step card
    card(
        title="Hello World 1!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        styles={ "card": {
                "width": "25%",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "text": {
                "font-family": "serif",
            }
        }

    )
    card(
        title="Hello World 2!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        styles={ "card": {
                "width": "25%",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "text": {
                "font-family": "serif",
            }
        }
    )
    card(
        title="Hello World 3!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        styles={ "card": {
                "width": "25%",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "text": {
                "font-family": "serif",
            }
        }
    )
    card(
        title="Hello World 4!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        styles={ "card": {
                "width": "25%",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "text": {
                "font-family": "serif",
            }
        }
    )


