import streamlit as st
from questions import questionnaire
from response import display_response
from figma import figma_welcome, figma_profile
from clinics import clinics
from streamlit_card import card

app_mode = "Welcome"



def main():
    # Set page config for wide mode
    st.set_page_config(
        page_title="PetalHealth",
        page_icon="https://www.svgrepo.com/show/287894/care.svg",
        menu_items={
            "About": "Welcome to PetalHealth, a revolutionary AI-assisted reproductive health resource center designed to empower you with personalized, comprehensive information that respects and responds to your unique reproductive health needs.",
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
        st.button("Personalized Advice", on_click=lambda: setattr(st.session_state, 'current_page', 'chat'))
        st.button("Clinics", on_click=lambda: setattr(st.session_state, 'current_page', 'clinics'))
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
    
    # set openai key
    st.session_state.openai_api_key = openai_api_key


    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'welcome'  # Default page

    if st.session_state['current_page'] == 'welcome':
        welcome_page()
    elif st.session_state['current_page'] == 'questions':
        questionnaire()
    elif st.session_state['current_page'] == 'chat':
        display_response(openai_api_key=openai_api_key)
    elif st.session_state['current_page'] == 'clinics':
        clinics()

def welcome_page():
    st.title("Welcome to PetalHealth!")

    st.image("asset/petal_cover.png")

    def create_card(title, text, is_active=False):
        return card(
            title=title,
            text=text,
            image=None,
            # image="http://placekitten.com/300/250",
            styles={ "card": {
                    "width": "100%",
            #         "background-color":"#ffffff",
                    # "height": "100px",
                    "filter": "drop-shadow(0px 23px 12px rgba(0,0,0,0.10000000149011612))",
                    "border-radius":"20px",
                    "margin": "20px",
                    "padding":"10px",
                    "display":"flex",
                    "flex-direction":"column",
            #         "gap":"30px",
                    "border":"1px solid blue" if is_active else "none",
                    "outline": "blue" if is_active else "none"
                    },
                    "text": {
                        "color": "#ccc"
                    },
                    "title": {
                        "color": "#eee"
                    },
                    "filter": {
                        "background-color": "#a8eb12",  # <- make the image not dimmed anymore  
                        "background-image": "linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%)"
                    }
            }

        )


    # st.header("Greetings")
    # st.write("Welcome to PetalHealth! We're excited to guide you through your personalized reproductive health journey. Our platform is designed to offer you tailored advice, clear information, and support that respects your unique needs and privacy. Get started today and take the first step towards informed and empowered health decisions. Thank you for trusting PetalHealth—where your health and privacy come first.")

    # st.header("Privacy")
    # st.info("At PetalHealth, your privacy is our top priority. To protect your personal information, our system only uses state-of-the-art security measures and adheres to the strictest data protection standards. We employ advanced encryption technologies to secure all data transmissions and store information in compliance with leading privacy laws, including HIPAA. Our platform is designed to ensure that your personal details are accessed only by authorized personnel and only for the purpose of enhancing your experience and providing the services you need.", icon="🔒")

    # st.header("Get Started")
    # st.success("Ready to explore your personalized reproductive health options? Click 'Get Started' to begin a journey tailored just for you. You’ll answer some simple questions to help us understand your needs and preferences. From there, we’ll provide you with customized advice and resources to make informed decisions about your health. Let’s take this step together—your empowered path starts now.", icon="🏃")

    col1, col2, col3 = st.columns(3)

    with col1:
        # st.markdown("#### Reproductive Health Education")
        # st.write("We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs.")
        create_card("Reproductive Health Education", "We provide the most accurate reproductive health information in an easy learning environment suited to different people's needs")

    with col2:
        # st.markdown("#### Shared Decision-Making")
        # st.write("We help you navigate important conversations through the lens of shared decision-making.")
        create_card("Shared Decision-Making", "We help you navigate important conversations through the lens of shared decision-making.")

    with col3:
        # st.markdown("#### Personalized Recommendations")
        # st.write("Based on your profile, we can provide personalized and precision reproductive health recommendations.")
        create_card("Personalized Recommendations", "Based on your profile, we can provide personalized and precision reproductive health recommendations.")
    
    st.button("Get Started", on_click=lambda: setattr(st.session_state, 'current_page', 'questions'))
        

if __name__ == "__main__":
    main()

