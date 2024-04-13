import streamlit as st

def main():
    
    st.set_page_config(
        page_title="EmpowerCare",
        page_icon="https://www.svgrepo.com/show/137210/health-care.svg",
        menu_items={"About": "Welcome to EmpowerCare, a revolutionary AI-assisted reproductive health resource center designed to empower you with personalized, comprehensive information that respects and responds to your unique reproductive health needs.", "Get help": None, "Report a Bug": None}
    )

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button("Welcome"):
        st.session_state['current_page'] = 'welcome'
    if st.sidebar.button("Questions"):
        st.session_state['current_page'] = 'questions'

    # Display pages based on sidebar navigation choices
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'welcome'  # Default page

    if st.session_state['current_page'] == 'welcome':
        welcome_page()
    elif st.session_state['current_page'] == 'questions':
        questions_page()


def welcome_page():
    st.title("Welcome to EmpowerCare!")

    st.header("Greetings")
    st.write("Welcome to EmpowerCare! We're excited to guide you through your personalized reproductive health journey. Our platform is designed to offer you tailored advice, clear information, and support that respects your unique needs and privacy. Get started today and take the first step towards informed and empowered health decisions. Thank you for trusting EmpowerCare—where your health and privacy come first.")

    st.header("Privacy")
    st.write("At EmpowerCare, your privacy is our top priority. To protect your personal information, our system only uses state-of-the-art security measures and adheres to the strictest data protection standards. We employ advanced encryption technologies to secure all data transmissions and store information in compliance with leading privacy laws, including HIPAA. Our platform is designed to ensure that your personal details are accessed only by authorized personnel and only for the purpose of enhancing your experience and providing the services you need.")

    st.header("Get Started")
    st.write("Ready to explore your personalized reproductive health options? Click 'Get Started' to begin a journey tailored just for you. You’ll answer some simple questions to help us understand your needs and preferences. From there, we’ll provide you with customized advice and resources to make informed decisions about your health. Let’s take this step together—your empowered path starts now.")

    if st.button("Get Started"):
        st.session_state.current_page = 'questions'

def questions_page():
    st.title("Reproductive Health Profile")

    # Personal Information
    st.header("Personal Information")
    age = st.number_input("What is your age?", min_value=12, max_value=100)
    gender_identity = st.selectbox("What is your gender identity?", ["Male", "Female", "Non-binary", "Prefer not to say"])
    zip_code = st.text_input("What is your zip code or city of residence?")
    employment_status = st.selectbox("What is your current employment status?", ["Employed", "Unemployed", "Student", "Retired"])

    # Health Status
    st.header("Health Status")
    general_health = st.selectbox("How would you describe your overall health?", ["Excellent", "Good", "Fair", "Poor"])
    currentl_medications = st.text_area("Are you currently taking any medications? If yes, please list them.")
    allergies = st.text_area("Do you have any known allergies or adverse reactions to medications?")
    known_conditions = st.text_area("Do you have any known health conditions that affect your reproductive health?")

    # Reproductive History
    st.header("Reproductive History")
    current_contraception = st.radio("Are you currently using any form of contraception?", ["Yes", "No"])
    past_contraception = st.text_area("Have you used any contraceptive methods in the past?")
    family_history = st.text_area("Have there been any fertility or pregnancy-related issues in your family history?")

    # Insurance Information
    st.header("Insurance Information")
    has_insurance = st.radio("Do you have health insurance?", ["Yes", "No"])
    insurance_provider = st.text_input("Which provider?")
    need_assistance = st.radio("Do you need assistance finding clinics that accept your insurance?", ["Yes", "No"])

    # Future Planning
    st.header("Future Planning")
    planning_family = st.radio("Are you considering starting or expanding your family in the near future?", ["Yes", "No"])
    conception_plan = st.text_input("If yes, have you thought about when you might want to start trying to conceive?")
    contraception_priority = st.text_area("What are your priorities when considering contraception?")

    # Preferences and Concerns
    st.header("Preferences and Concerns")
    fertility_concerns = st.text_area("What concerns do you have regarding contraceptive methods affecting your fertility?")
    cultural_concerns = st.text_area("Are there cultural or ethical considerations that we should take into account when providing you with health information?")
    learning_preferences = st.selectbox("What are your preferences for learning about health topics?", ["Reading articles", "Watching videos", "Speaking to a professional", "Other"])
    consultation_interest = st.radio("Would you be interested in a follow-up consultation with a healthcare provider?", ["Yes", "No"])

    # Feedback and Consent
    st.header("Privacy and Consent")
    consent = st.radio("Do you consent to have this information used to tailor health advice specifically for you?", ["Yes", "No"])

    if st.button("Submit"):
        st.success("Profile Submitted Successfully!")

if __name__ == "__main__":
    main()
