import streamlit as st
from questions import questionnaire
from response import display_response
from figma import figma_welcome, figa_profile

app_mode = "Welcome"



def main():
    # Set page config for wide mode
    st.set_page_config(
        page_title="EmpowerCare",
        page_icon="https://www.svgrepo.com/show/287894/care.svg",
        menu_items={
            "About": "Welcome to EmpowerCare, a revolutionary AI-assisted reproductive health resource center designed to empower you with personalized, comprehensive information that respects and responds to your unique reproductive health needs.",
            "Get help": None,
            "Report a Bug": None
        },
        layout="wide"
    )

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")

    # st.sidebar.title("Navigation")
    # app_mode = st.sidebar.selectbox("Choose the section", ["Welcome", "Fill Questionnaire", "Chat", "Figma"])
    # Sidebar navigation
    with st.sidebar:
        st.image("asset/petal-logo-w.png")
        st.markdown("## Navigation")
        st.button("Home", on_click=lambda: setattr(st.session_state, 'current_page', 'welcome'))
        st.button("Profile", on_click=lambda: setattr(st.session_state, 'current_page', 'questions'))
        st.button("Get Care", on_click=lambda: setattr(st.session_state, 'current_page', 'chat'))
        st.button("Privacy", on_click=lambda: setattr(st.session_state, 'current_page', 'figma'))
        st.button("Partners", on_click=lambda: setattr(st.session_state, 'current_page', 'partners'))
        st.button("Help", on_click=lambda: setattr(st.session_state, 'current_page', 'help'))

        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")

    # if app_mode == "Welcome":
    #     st.session_state.current_page = 'welcome'
    # elif app_mode == "Fill Questionnaire":
    #     st.session_state.current_page = 'questions'
    # elif app_mode == "Chat":
    #     st.session_state.current_page = 'chat'
    # elif app_mode == "Figma":
    #     st.session_state.current_page = 'figma'
    
    # make sure profile is updated


    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'welcome'  # Default page

    if st.session_state['current_page'] == 'welcome':
        welcome_page()
    elif st.session_state['current_page'] == 'questions':
        questionnaire()
    elif st.session_state['current_page'] == 'chat':
        display_response(openai_api_key=openai_api_key)
    elif st.session_state['current_page'] == 'figma':
        figa_profile()

def welcome_page():
    st.title("Welcome to EmpowerCare!")

    st.header("Greetings")
    st.write("Welcome to EmpowerCare! We're excited to guide you through your personalized reproductive health journey. Our platform is designed to offer you tailored advice, clear information, and support that respects your unique needs and privacy. Get started today and take the first step towards informed and empowered health decisions. Thank you for trusting EmpowerCare—where your health and privacy come first.")

    st.header("Privacy")
    st.info("At EmpowerCare, your privacy is our top priority. To protect your personal information, our system only uses state-of-the-art security measures and adheres to the strictest data protection standards. We employ advanced encryption technologies to secure all data transmissions and store information in compliance with leading privacy laws, including HIPAA. Our platform is designed to ensure that your personal details are accessed only by authorized personnel and only for the purpose of enhancing your experience and providing the services you need.", icon="🔒")

    st.header("Get Started")
    st.success("Ready to explore your personalized reproductive health options? Click 'Get Started' to begin a journey tailored just for you. You’ll answer some simple questions to help us understand your needs and preferences. From there, we’ll provide you with customized advice and resources to make informed decisions about your health. Let’s take this step together—your empowered path starts now.", icon="🏃")

    st.button("Get Started", on_click=lambda: setattr(st.session_state, 'current_page', 'questions'))
        

if __name__ == "__main__":
    main()

