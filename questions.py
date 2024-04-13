import streamlit as st

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
        # st.write(f'Page {st.session_state.page_number+1} of {len(questionnaire_pages)}')
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

