import streamlit as st

def main():
    st.set_page_config(
        page_title="EmpowerCare",
        page_icon="https://www.svgrepo.com/show/287894/care.svg",
        menu_items={
            "About": "Welcome to EmpowerCare, a revolutionary AI-assisted reproductive health resource center designed to empower you with personalized, comprehensive information that respects and responds to your unique reproductive health needs.",
            "Get help": None,
            "Report a Bug": None
        }
    )

    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the section", ["Welcome", "Fill Questionnaire"])

    if app_mode == "Welcome":
        st.session_state.current_page = 'welcome'
    elif app_mode == "Fill Questionnaire":
        st.session_state.current_page = 'questions'
    
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'welcome'  # Default page

    if st.session_state['current_page'] == 'welcome':
        welcome_page()
    elif st.session_state['current_page'] == 'questions':
        questionnaire()



def welcome_page():
    st.title("Welcome to EmpowerCare!")

    st.header("Greetings")
    st.write("Welcome to EmpowerCare! We're excited to guide you through your personalized reproductive health journey. Our platform is designed to offer you tailored advice, clear information, and support that respects your unique needs and privacy. Get started today and take the first step towards informed and empowered health decisions. Thank you for trusting EmpowerCare—where your health and privacy come first.")

    st.header("Privacy")
    st.write("At EmpowerCare, your privacy is our top priority. To protect your personal information, our system only uses state-of-the-art security measures and adheres to the strictest data protection standards. We employ advanced encryption technologies to secure all data transmissions and store information in compliance with leading privacy laws, including HIPAA. Our platform is designed to ensure that your personal details are accessed only by authorized personnel and only for the purpose of enhancing your experience and providing the services you need.")

    st.header("Get Started")
    st.write("Ready to explore your personalized reproductive health options? Click 'Get Started' to begin a journey tailored just for you. You’ll answer some simple questions to help us understand your needs and preferences. From there, we’ll provide you with customized advice and resources to make informed decisions about your health. Let’s take this step together—your empowered path starts now.")

    def go_to_questions():
        st.session_state.current_page = 'questions'
        main()
        
    st.button("Get Started", on_click=go_to_questions)


def collect_personal_info():
    # Personal Information
    age = st.number_input("What is your age?", min_value=12, max_value=100, key="age")
    gender_identity = st.selectbox("What is your gender identity?", ["Male", "Female", "Non-binary", "Prefer not to say"], key="gender")
    zip_code = st.text_input("What is your zip code or city of residence?")
    employment_status = st.selectbox("What is your current employment status?", ["Employed", "Unemployed", "Student", "Retired"])

    navigate()

def collect_health_status():
    # Health Status
    general_health = st.selectbox("How would you describe your overall health?", ["Excellent", "Good", "Fair", "Poor"], key="health")
    currentl_medications = st.radio("Are you currently taking any medications?", ["Yes", "No"], key="currentl_medications")
    if st.session_state.currentl_medications == "Yes":
        currentl_medications = st.text_area("Types of medications being used", key="medication_types")
    allergies = st.radio("Do you have any known allergies or adverse reactions to medications?", ["Yes", "No"], key="allergies")
    if st.session_state.allergies == "Yes":
        allergies = st.text_area("List of allergies")
    known_conditions = st.radio("Do you have any known health conditions that affect your reproductive health?", ["Yes", "No"], key="known_conditions")
    if st.session_state.known_conditions == "Yes":
        known_conditions = st.text_area("List health conditions")

    navigate()

def collect_reproductive_history():
    # Reproductive History
    current_contraception_q = st.radio("Are you currently using any form of contraception?", ["Yes", "No"])
    if current_contraception_q == "Yes":
        current_contraception = st.text_area("Types of contraception being used")
    past_contraception_q = st.radio("Have you used any contraceptive methods in the past?", ["Yes", "No"])
    if past_contraception_q == "Yes":
        past_contraception = st.text_area("Types of contraception used")
    family_history_q = st.radio("Have there been any fertility or pregnancy-related issues in your family history?", ["Yes", "No"])
    if family_history_q == "Yes":
        family_history = st.text_area("Details")

    navigate()

def collect_insurance_info():
    # Insurance Information
    insurance_provider_q = st.radio("Do you have health insurance?", ["Yes", "No"])
    if insurance_provider_q == "Yes":
        insurance_provider = st.text_input("Which provider?")
    need_assistance = st.radio("Do you need assistance finding clinics that accept your insurance?", ["Yes", "No"])

    navigate()

def collect_future_planning():
    # Future Planning
    planning_family_q = st.radio("Are you considering starting or expanding your family in the near future?", ["Yes", "No"])
    if planning_family_q == "Yes":
        conception_plan = st.text_input("Have you thought about when you might want to start trying to conceive?")
        contraception_priority = st.text_area("What are your priorities when considering contraception?")

    navigate()

def preferences_concerns():
    # Preferences and Concerns
    fertility_concerns = st.text_area("What concerns do you have regarding contraceptive methods affecting your fertility?")
    cultural_concerns = st.text_area("Are there cultural or ethical considerations that we should take into account when providing you with health information?")
    learning_preferences = st.selectbox("What are your preferences for learning about health topics?", ["Reading articles", "Watching videos", "Speaking to a professional", "Other"])
    consultation_interest = st.radio("Would you be interested in a follow-up consultation with a healthcare provider?", ["Yes", "No"])
    
    navigate()

def privacy_concent():
    # Feedback and Consent
    consent = st.radio("Do you consent to have this information used to tailor health advice specifically for you?", ["Yes", "No"])
    if st.button("Finish"):
        st.success("Profile Submitted Successfully!")
        st.session_state.current_page = 'chat'

questionnaire_pages = [
        ("Personal Information", collect_personal_info),
        ("Health Status", collect_health_status),
        ("Reproductive History", collect_reproductive_history),
        ("Insurance Information", collect_insurance_info),
        ("Future Planning", collect_future_planning),
        ("Preferences", preferences_concerns),
        ("Privacy", privacy_concent)
    ]
    
def questionnaire():

    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0

    if st.session_state.page_number < len(questionnaire_pages):
        page_title, page_function = questionnaire_pages[st.session_state.page_number]
        st.progress((st.session_state.page_number + 1) / len(questionnaire_pages))
        st.header(page_title)
        st.write(f'Page {st.session_state.page_number+1} of {len(questionnaire_pages)}')
        page_function()
    else:
        st.session_state.page_number = 0  # Reset for reusability

def navigate():
    def prev():
        if st.session_state.page_number > 0:
            st.session_state.page_number -= 1
    def next():
        if st.session_state.page_number < len(questionnaire_pages) - 1:
            st.session_state.page_number += 1

    col1, _, _,_,_, col2 = st.columns(6)

    col1.button("Back", on_click=prev)
    col2.button("Next", on_click=next)


if __name__ == "__main__":
    main()

