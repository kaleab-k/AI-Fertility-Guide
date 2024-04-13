import streamlit as st

def collect_personal_info():
    # Personal Information
    st.number_input("What is your age?", min_value=12, max_value=100, key="age")
    st.selectbox("What is your gender identity?", ["Male", "Female", "Non-binary", "Prefer not to say"], key="gender")
    st.text_input("What is your zip code or city of residence?", key="zip_code")
    st.selectbox("What is your current employment status?", ["Employed", "Unemployed", "Student", "Retired"], key="employment_status")

    navigate()

def collect_health_status():
    # Health Status
    st.selectbox("How would you describe your overall health?", ["Excellent", "Good", "Fair", "Poor"], key="health")
    st.radio("Are you currently taking any medications?", ["Yes", "No"], key="current_medications")
    if st.session_state.current_medications == "Yes":
        st.text_area("Types of medications being used", key="medication_types")
    st.radio("Do you have any known allergies or adverse reactions to medications?", ["Yes", "No"], key="allergies")
    if st.session_state.allergies == "Yes":
        st.text_area("List of allergies", key="allergies_list")
    st.radio("Do you have any known health conditions that affect your reproductive health?", ["Yes", "No"], key="known_conditions")
    if st.session_state.known_conditions == "Yes":
        st.text_area("List health conditions", key="known_conditions_list")

    navigate()

def collect_reproductive_history():
    # Reproductive History
    st.radio("Are you currently using any form of contraception?", ["Yes", "No"], key="current_contraception")
    if st.session_state.current_contraception == "Yes":
        st.text_area("Types of contraception being used", key="current_contraception_types")
    st.radio("Have you used any contraceptive methods in the past?", ["Yes", "No"], key="past_contraception")
    if st.session_state.past_contraception == "Yes":
        st.text_area("Types of past contraception used", key="past_contraception_types")
    st.radio("Have there been any fertility or pregnancy-related issues in your family history?", ["Yes", "No"], key="family_history")
    if st.session_state.family_history == "Yes":
        st.text_area("Details of fertility or pregnancy-related issues in your family", key="family_history_details")

    navigate()

def collect_insurance_info():
    # Insurance Information
    st.radio("Do you have health insurance?", ["Yes", "No"], key="insurance_status")
    if st.session_state.insurance_status == "Yes":
        st.text_input("Which provider?", key="insurance_provider")
    st.radio("Do you need assistance finding clinics that accept your insurance?", ["Yes", "No"], key="need_assistance")

    navigate()

def collect_future_planning():
    # Future Planning
    st.radio("Are you considering starting or expanding your family in the near future?", ["Yes", "No"], key="planning_family")
    if st.session_state.planning_family == "Yes":
        st.text_input("Have you thought about when you might want to start trying to conceive?", key="conception_plan")
        st.text_area("What are your priorities when considering contraception?", key="contraception_priority")

    navigate()

def preferences_concerns():
    # Preferences and Concerns
    st.text_area("What concerns do you have regarding contraceptive methods affecting your fertility?", key="fertility_concerns")
    st.text_area("Are there cultural or ethical considerations that we should take into account when providing you with health information?", key="cultural_concerns")
    st.selectbox("What are your preferences for learning about health topics?", ["Reading articles", "Watching videos", "Speaking to a professional", "Other"], key="learning_preferences")
    st.radio("Would you be interested in a follow-up consultation with a healthcare provider?", ["Yes", "No"], key="consultation_interest")
    
    navigate()

def privacy_concent():
    # Feedback and Consent
    st.radio("Do you consent to have this information used to tailor health advice specifically for you?", ["Yes", "No"], key="consent")
    if st.button("Finish"):
        user_data = compile_user_data()
        st.success("Profile Submitted Successfully!")
        st.info(user_data)
        # st.session_state.current_page = 'chat'
        

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

def compile_user_data():
    # Gather user data from Streamlit's session state
    user_data = {
        'age': st.session_state.get('age', 'Not specified'),
        'gender': st.session_state.get('gender', 'Not specified'),
        'location': st.session_state.get('zip_code', 'Not specified'),
        'employment_status': st.session_state.get('employment_status', 'Not specified'),
        'health_status': st.session_state.get('health', 'Not specified'),
        'current_medications': 'Yes' if st.session_state.get('current_medications', 'No') == 'Yes' else 'No',
        'medication_types': st.session_state.get('medication_types', 'None'),
        'allergies_list': st.session_state.get('allergies_list', 'None'),
        'known_conditions_list': st.session_state.get('known_conditions_list', 'None'),
        'current_contraception': 'Yes' if st.session_state.get('current_contraception', 'No') == 'Yes' else 'No',
        'current_contraception_types': st.session_state.get('current_contraception_types', 'None'),
        'past_contraception': 'Yes' if st.session_state.get('past_contraception', 'No') == 'Yes' else 'No',
        'past_contraception_types': st.session_state.get('past_contraception_types', 'None'),
        'family_history': 'Yes' if st.session_state.get('family_history', 'No') == 'Yes' else 'No',
        'family_history_details': st.session_state.get('family_history_details', 'None'),
        'insurance_provider': st.session_state.get('insurance_provider', 'Not insured'),
        'need_assistance': st.session_state.get('need_assistance', 'No'),
        'planning_family': st.session_state.get('planning_family', 'No'),
        'conception_plan': st.session_state.get('conception_plan', 'Not specified'),
        'contraception_priority': st.session_state.get('contraception_priority', 'Not specified'),
        'fertility_concerns': st.session_state.get('fertility_concerns', 'None specified'),
        'cultural_concerns': st.session_state.get('cultural_concerns', 'None specified'),
        'learning_preferences': st.session_state.get('learning_preferences', 'No preference'),
        'consultation_interest': st.session_state.get('consultation_interest', 'No'),
        'consent': st.session_state.get('consent', 'No')
    }

    return user_data