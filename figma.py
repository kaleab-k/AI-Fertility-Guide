import streamlit as st
from streamlit_card import card

def create_card(title, text, another_text, is_active=False):
    return card(
        title=title,
        text=text,
        image=None,
        # image="http://placekitten.com/300/250",
        styles={ "card": {
                "width": "100%",
        #         "background-color":"#ffffff",
                "height": "100px",
                "filter": "drop-shadow(0px 23px 12px rgba(0,0,0,0.10000000149011612))",
                "border-radius":"20px",
        #         "padding":"40px",
                "display":"flex",
                "flex-direction":"column",
        #         "gap":"30px",
                "border":"1px solid blue" if is_active else "none",
                "outline": "blue" if is_active else "none"
                },
                "text": {
                    "color": "#333"
                },
                "title": {
                    "color": "#111"
                },
                 "filter": {
                    "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore  
                }
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
    

# Custom function to generate a card for each step
def step_card(title, description, button_label, is_active):
    card_color = "primary" if is_active else "secondary"
    button_outcome = st.button if is_active else st.empty  # Only active cards will have a functioning button
    
    with st.container():
        with card(card_color):
            st.markdown(f"### {title}")
            st.write(description)
            button_outcome(button_label)


def figma_profile():
    # Function to create a single step car

    # Title and subtitle
    st.title("Start Your MOJO Plan")
    st.header("A personalized reproductive health questionnaire & plan.")

    # Cards for each step
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_card("STEP 1", "Tell us how we can help.", "Start Here", True)
    with col2:
        create_card("STEP 2", "Tell us about yourself.", "In Progress", False)
    with col3:
        create_card("STEP 3", "Learn about your options.", "Pending", False)
    with col4:
        create_card("STEP 3", "Empower your decisions.", "Pending", False)
