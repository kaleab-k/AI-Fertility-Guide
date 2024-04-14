import streamlit as st

def figma_ui():
    # Defining the layout using columns and sidebar
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Mojo_%28magazine%29_Logo.svg/1280px-Mojo_%28magazine%29_Logo.svg.png")
        st.markdown("## Screen 1")
        st.button("Learn")
        st.button("Resources")
        st.button("Get Care")
        st.button("Messages")
        st.button("Privacy")
        st.button("Patient Data")
        st.button("Partners")
        st.button("Help")

    # Main section with user profile and search bar
    user_name = "Thomas Anree"
    st.sidebar.text(user_name)

    search_bar = st.text_input("", placeholder="Ask or upload anything...")

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
