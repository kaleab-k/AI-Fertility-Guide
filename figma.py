import streamlit as st

def figma_ui():
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
        html_string = '''
            <div id="group1" class="group1">
            <div id="rectangle3" class="rectangle3">
            </div>
            <img id="pie-chart" class="pie-chart" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJPSURBVHgB1ViNVcIwED58DsAGZgPcwG4gG1AnkA3ACcAJihOgExQnACegTlA2OC/k8jhiSpP+8PR77whN7ufrJW2uAfhjGEAkEHFITUoyIklIhiwWO5KC5INkMxgMCugDRCQhyTEeOckYugI5U+gnUnJ/7gTPecxHTEEbkINnx7n+v9TZEjqJGHf7Vx5iU2gCMpw5jjSRoUfPS0iMKw+xGcTAIVP6AoUSEnopnmc7jBRPk8Uea+Y9lBDrKvYZNn1sUIaSiSXkiVFejEGDmXAe9KjGEmKbsbDJQxxnEIgmhNhufdHOUVAQiBaEVGWWnMHg7LQhxLYyCcdXyg2PJULvDa6HV/E/1T+W0AO3B9oMN3AlcKwDX44kIcXtDq6PgttE/9zyxb0djV0H0rYhvtjHaVvC7rBHs0WoQDI69tIa6+sb6BaKRD+lmliGYS/Xg7w4VoxkWIJJ2SfJHJpBB3+E03q0KEg2JC++6pFir6iZHMkQbOeWs7aFlsDqOgg5ztmU4qnA256x5E692Q2hA2g/HDyvIJcxebvRvkvjqVBMoGPgqUjbYzVS924s1tAjLkypchXzysH+iFnkdQq9ZonjZbXLxMnSBHoCmsVef/MYU142J+PW1arOQLLfd0kKY4t8YTh3SKXQEmjqaPkZNI+xd0khL0IFkUDzSskcX3NoAjQvzNJDLAmw1U/tAn9/il+cptrjGM7KAszmKaF3aXv08s19d2A21/P6xmBD8tTZ8Qy2O45JQuM0ObBSYMpNW2q4FWMBJhu6ElxRRg7wn/EDZUQqMPCbxMIAAAAASUVORK5CYII=">
            </div>
        '''
        st.markdown(html_string, unsafe_allow_html=True)

        st.markdown("#### Reproductive Health Education")
        st.write("We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs.")

    with col2:
        st.markdown("#### Shared Decision-Making")
        st.write("We help you navigate important conversations through the lens of shared decision-making.")

    with col3:
        st.markdown("#### Personalized Recommendations")
        st.write("Based on your profile, we can provide personalized and precision reproductive health recommendations.")
