import streamlit as st
from io import BytesIO
from assistant import PetalAssitant

import base64

# def text_to_speech(response):
#     tts = gTTS(text=response, lang='en', slow=False)
#     audio_buffer = BytesIO()
#     tts.write_to_fp(audio_buffer)
#     audio_buffer.seek(0)
#     return audio_buffer



def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


# from assistant import generate_response
from questions import compile_user_data

def display_response(user_data=None, openai_api_key=None):


    if user_data is None:
        user_data = compile_user_data()
    
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    if 'profile_updated' not in st.session_state:
        st.info("Please update your profile first to continue.")
        st.stop()

    with st.sidebar:
        st.header("Feedback on Advice")
        st.write("Please help us improve our advice by providing your feedback.")

        # User feedback collection
        feedback = st.text_area("Your feedback:", help="Describe what you found useful or not useful in the advice provided.")
        feedback_submitted = st.button("Submit Feedback")

        if feedback_submitted:
            st.success("Thank you for your feedback!")
            # Here you would typically send the feedback to a database or a file system for analysis
            save_feedback(user_data, feedback)
        

    st.title("💬 Your Personalized Advice")
    st.caption("🚀 PetalHealth Chatbot powered by OpenAI LLM")
    # Assuming generate_advice is a function that sends data to OpenAI and gets a response
    assistant = PetalAssitant(openai_api_key)
    response = assistant.generate_response(user_data, openai_api_key)

    ## convert to speech
    assistant.text_to_speech(response, "nova")
    # audio_file = open("audio.mp3", 'rb')
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format='audio/mpeg')
    autoplay_audio("audio.mp3")

    # st.write(response)
    st.chat_message("assistant").write(response)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I further assist you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        # client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = assistant.chat(messages=st.session_state.messages)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

def save_feedback(user_data, feedback):
    # Placeholder for saving feedback
    # In practice, this should save the feedback to a database or send it to an analytics server
    pass
