import streamlit as st

def main():
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
