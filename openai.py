
import openai

openai.api_key = 'your-api-key-here'

def create_openai_assistant_prompt(user_data):
    # Detailed description of the user's situation and needs
    prompt = f"""
    User Profile:
    - Age: {user_data['age']}
    - Gender: {user_data['gender']}
    - Health Status: {user_data['health_status']}
    - Location: {user_data['location']}
    - Insurance Provider: {user_data['insurance_provider']}
    
    User Needs:
    1. Contraception Advice:
       - Preferences: {user_data['contraception_preferences']}
       - Concerns about side effects: {user_data['contraception_side_effects']}
    
    2. Fertility Planning:
       - Planning Timeline: {user_data['family_planning_timeline']}
       - Fertility Concerns: {user_data['fertility_concerns']}
       - Family History: {user_data['family_history_of_fertility_issues']}
    
    3. Insurance and Clinic Navigation:
       - Needed Services: {user_data['required_services']}
    
    Task:
    - Provide detailed advice on suitable contraception options based on the user's health status and preferences.
    - Offer guidance on fertility planning considering the user's timeline and concerns.
    - Suggest local clinics that accept the user's insurance and offer the required services.
    """

    return prompt

def generate_response(user_data):

    prompt = create_openai_assistant_prompt(user_data)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500,  # Adjust based on the expected length of the response
        temperature=0.5   # A lower temperature for more focused and deterministic output
    )
    
    return response.choices[0].text.strip()

