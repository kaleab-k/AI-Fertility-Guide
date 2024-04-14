
from openai import OpenAI
from pathlib import Path


class PetalAssitant:

    def __init__(self, api_key) -> None:
        self.api_key = api_key

        self.client = self.get_client()
        self.assistant = self.create_assistant()

    def create_openai_assistant_prompt(self, user_data):

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


    def get_client(self):
        return OpenAI(api_key=self.api_key)
    
    def create_assistant(self):
        assistant = self.client.beta.assistants.create(
            name="Petal Health Agent",
            instructions="You are an expert in reproductive health and personalized medical consultation. Your task is to interact with users in a sensitive and informative manner to collect detailed personal and medical information. Use this information to provide tailored advice on contraception, fertility planning, and healthcare navigation. ",
            # tools=[{"type": "code_interpreter"}],
            model="gpt-4-turbo",
        )

        return assistant


    def generate_response(self, user_data, api_key):

        prompt = self.create_openai_assistant_prompt(user_data)

        # response = self.client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "assistant", "content": prompt}])
        thread = self.client.beta.threads.create()
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="assistant",
            content=prompt
        )
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=self.assistant.id,
            instructions=prompt
        )

        if run.status == 'completed': 
            messages = self.client.beta.threads.messages.list(
                thread_id=thread.id
            )
            print(messages)
            return messages

            return response.choices[0].message.content
    
    def chat(self, messages):
        response = self.client.chat.completions.create(model="gpt-4-turbo", messages=messages)

        return response.choices[0].message.content
    
    def get_clinics(self, zip_code):
        prompt = f"Povide longitude and latitude of local clinics in the area of the zipcode of {zip_code} in python dictionary format only. Do not provide any other text. No intro text. No description. "
        prompt += '''Here is an example for the format:  
                    { 
                    "clinics": [
                        {
                            "name": "Health Care Clinic",
                            "lat": 37.7749,
                            "lon": -122.4194,
                            "services_offered": ["General Health", "Specialty Care"],
                        }
                    ]}
                 '''
        response = self.client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "assistant", "content": prompt}])

        return response.choices[0].message.content

    def text_to_speech(self, text, voice):
        speech_file_path = Path("audio.mp3")
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        response.stream_to_file(speech_file_path)

    def transcribe(self, audio_path):
        audio_file= open(audio_path, "rb")

        transcription = self.client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

        return transcription.text
