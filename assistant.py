
import openai

def create_openai_assistant_prompt(user_data, api_key):

    oepnai.api_key = api_key
    # Constructing a detailed prompt based on the comprehensive user data collected
    prompt = f"""
    User Profile:
    - Age: {user_data['age']}
    - Gender: {user_data['gender']}
    - General Health: {user_data['health_status']}
    - Location: {user_data['location']}
    - Employment Status: {user_data['employment_status']}
    - Insurance Provider: {user_data.get('insurance_provider', 'Not insured')}
    
    User Needs:
    """

    if user_data['current_medications'] == 'Yes' and user_data.get('medication_types'):
        prompt += f"- Current Medications: {user_data['medication_types']}\n"
    else:
        prompt += "- Current Medications: No\n"

    if user_data.get('allergies_list'):
        prompt += f"- Known Allergies: {user_data['allergies_list']}\n"
    else:
        prompt += "- Known Allergies: None\n"

    if user_data.get('known_conditions_list'):
        prompt += f"- Reproductive Health Conditions: {user_data['known_conditions_list']}\n"
    else:
        prompt += "- Reproductive Health Conditions: None\n"

    prompt += "\n1. Contraception Advice:\n"
    if user_data['current_contraception'] == 'Yes':
        prompt += f"   - Current Contraception: {user_data.get('current_contraception_types', 'Not specified')}\n"
    else:
        prompt += "   - Current Contraception: No\n"

    if user_data['past_contraception'] == 'Yes':
        prompt += f"   - Past Contraception Use: {user_data.get('past_contraception_types', 'Not specified')}\n"
    else:
        prompt += "   - Past Contraception Use: No\n"

    prompt += f"   - Priorities for Contraception: {user_data.get('contraception_priority', 'Not specified')}\n"
    prompt += "\n2. Fertility Planning:\n"
    prompt += f"   - Considering Expanding Family: {user_data.get('planning_family', 'No')}\n"
    prompt += f"   - Planned Conception Timeline: {user_data.get('conception_plan', 'Not specified')}\n"
    prompt += f"   - Fertility Concerns: {user_data.get('fertility_concerns', 'None specified')}\n"

    if user_data['family_history'] == 'Yes':
        prompt += f"   - Family Fertility History: {user_data.get('family_history_details', 'No issues reported')}\n"
    else:
        prompt += "   - Family Fertility History: No issues reported\n"

    prompt += "\n3. Insurance and Clinic Navigation:\n"
    prompt += f"   - Needs Clinic Assistance: {user_data.get('need_assistance', 'No')}\n"

    prompt += "\n4. Cultural and Ethical Considerations:\n"
    prompt += f"   - Cultural or Ethical Concerns: {user_data.get('cultural_concerns', 'None specified')}\n"

    prompt += f"\nTask:\n"
    prompt += "- Provide detailed advice on suitable contraception options considering the user's health, current medication, past experiences, and priorities.\n"
    prompt += "- Offer guidance on fertility planning considering the user's timeline, concerns, and family history.\n"
    prompt += "- Suggest local clinics that accept the user's insurance and offer required services, considering any cultural or ethical preferences.\n"
    prompt += "- Include personalized learning resources based on the user's preferred learning method: {user_data.get('learning_preferences', 'No preference')}.\n"

    return prompt


def generate_response(user_data, api_key):

    prompt = create_openai_assistant_prompt(user_data, api_key)
    response = oepnai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500,  # Adjust based on the expected length of the response
        temperature=0.5   # A lower temperature for more focused and deterministic output
    )

    return response.choices[0].text.strip()

