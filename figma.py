import streamlit as st
from streamlit_card import card

def create_card(title, text):
    return card(
        title=title,
        text=text,
        image=None,
        # image="http://placekitten.com/300/250",
        styles={ "card": {
                "width": "100%",
                "background-color":"#ffffff",
                "height": "320px",
                "filter": "drop-shadow(0px 23px 12px rgba(0,0,0,0.10000000149011612))",
                "border-radius":"20px",
                "padding":"40px",
                "display":"flex",
                "flex-direction":"column",
                "gap":"30px",
                "border-style":"hidden",
                "outline": "none"
                },
        }
    )

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
        # st.markdown("#### Reproductive Health Education")
        # st.write("We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs.")
        create_card("Reproductive Health Education", "We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs")

    with col2:
        # st.markdown("#### Shared Decision-Making")
        # st.write("We help you navigate important conversations through the lens of shared decision-making.")
        create_card("Shared Decision-Making", "We help you navigate important conversations through the lens of shared decision-making.")

    with col3:
        # st.markdown("#### Personalized Recommendations")
        # st.write("Based on your profile, we can provide personalized and precision reproductive health recommendations.")
        create_card("Personalized Recommendations", "Based on your profile, we can provide personalized and precision reproductive health recommendations.")
    
def figa_profile():
    # Function to create a single step card
    
    col1, col2, col3 = st.columns(3)

    with col1:
        create_card("Hello World 1!", "Some description")
    with col2:
        create_card("Hello World 2!", "Some description")
    with col3:
        create_card("Hello World 3!", "Some description")

