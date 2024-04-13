import streamlit as st
from assistant import generate_response
from questions import compile_user_data

def display_response(user_data=None, openai_api_key=None):
    if user_data is None:
        user_data = compile_user_data()

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
    st.caption("🚀 EmpowerCare Chatbot powered by OpenAI LLM")
    # Assuming generate_advice is a function that sends data to OpenAI and gets a response
    client, response = generate_response(user_data, openai_api_key)
    # st.write(response)
    st.chat_message("assistant").write(user_data)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I further assist you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        # if not openai_api_key:
        #     st.info("Please add your OpenAI API key to continue.")
        #     st.stop()

        # client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg =  response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

def save_feedback(user_data, feedback):
    # Placeholder for saving feedback
    # In practice, this should save the feedback to a database or send it to an analytics server
    pass
