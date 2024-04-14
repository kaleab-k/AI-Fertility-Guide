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
    def create_card(title, text):
        return card(
            title=title,
            text=text,
            image="http://placekitten.com/300/250",
            styles={ "card": {
                    "width": "100%",
                    "border-radius": "60px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "text": {
                    "font-family": "serif",
                }
            }
        )
    
    col1, col2, col3 = st.columns(3)

    with col1:
        create_card("Hello World 1!", "Some description")
    with col2:
        create_card("Hello World 2!", "Some description")
    with col3:
        create_card("Hello World 3!", "Some description")

