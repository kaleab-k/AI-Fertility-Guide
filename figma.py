import streamlit as st

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
    def create_step_card(step_number, title, status, is_active):
        # Custom styles for the active card
        if is_active:
            border_color = "blue"
            background_color = "#e0eaff"
        else:
            border_color = "rgba(0, 0, 0, 0.1)"
            background_color = "#ffffff"
            
        # Define the card layout and content
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.markdown(f"""
                    <div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px; background-color: {background_color}">
                        <h4 style="color: {border_color};">STEP {step_number}</h4>
                        <p>{title}</p>
                        {f'<button class="st-btn primary">Start Here</button>' if is_active else f'<p>{status}</p>'}
                    </div>
                    """, unsafe_allow_html=True)

    # Title and subtitle
    st.title("Start Your MOJO Plan")
    st.header("A personalized reproductive health questionnaire & plan.")

    # Steps
    with st.container():
        create_step_card(1, "Tell us how we can help.", "Start Here", is_active=True)
        create_step_card(2, "Tell us about yourself.", "In Progress", is_active=False)
        create_step_card(3, "Learn about your options.", "Pending", is_active=False)
        create_step_card(3, "Empower your decisions.", "Pending", is_active=False)

