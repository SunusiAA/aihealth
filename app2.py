import streamlit as st
import requests

# Define Rasa server URL
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Adding a health logo at the top
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGvR190r1vu82lCCI9ZNPRG2hmERU_9mdf4Q&s", width=100)

st.title("AI Healthcare Chat Bot")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Welcome to AI Innovation")
    st.write("Chat with our healthcare agent to improve your health.")

with col2:
    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Function to send message to Rasa server
    def send_message(message):
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": message})
        if response.status_code == 200:
            return response.json()
        else:
            return []

    # Get user input
    user_input = st.text_input("You: ", "")

    # Handle message send button
    if st.button("Send"):
        if user_input:
            st.session_state['messages'].append({"message": user_input, "is_user": True})
            responses = send_message(user_input)
            for response in responses:
                st.session_state['messages'].append({"message": response['text'], "is_user": False})

    # Display chat history
    for msg in st.session_state['messages']:
        if msg['is_user']:
            st.write(f"You: {msg['message']}")
        else:
            st.write(f"Bot: {msg['message']}")

# Sidebar menu
st.sidebar.header("Menu")
menu_option = st.sidebar.selectbox("Choose an option", ["About Us", "Start Charting", "End Charting"])

if menu_option == "About Us":
    description = """
    ### About AI Healthcare Innovation

    The AI Healthcare Chat Bot is an innovative and intelligent virtual assistant designed to provide users with immediate, personalized health care advice and support. Leveraging advanced natural language processing and machine learning technologies, this chatbot can understand and respond to a wide range of health-related queries, making health care more accessible and convenient.

    **Key Features:**
    - **24/7 Availability:** Provides round-the-clock assistance, ensuring users have access to health care support anytime.
    - **Symptom Checker:** Users can input their symptoms, and the chatbot will offer potential causes and advice on the next steps.
    - **Medical Information:** Delivers accurate and up-to-date information on various medical conditions, treatments, and medications.

    **Technologies Used:**
    - **Natural Language Processing (NLP):** For understanding and generating human-like text.
    - **Machine Learning (ML):** To improve the accuracy and relevance of responses over time.
    - **Secure Data Handling:** Ensuring compliance with health care data protection standards.

    The AI Healthcare Chat Bot aims to revolutionize the way individuals access health care information and support, providing a reliable, efficient, and user-friendly solution for managing health concerns.
    """
    st.sidebar.markdown(description)

elif menu_option == "Start Charting":
    st.sidebar.write("Charting started")

elif menu_option == "End Charting":
    st.sidebar.markdown('<i class="fa fa-thumbs-up" style="font-size:24px;color:green;"></i>', unsafe_allow_html=True)
    st.sidebar.write("Charting ended")

# Adding CSS for the Font Awesome icons
st.markdown("""
    <style>
    .fa {
        font-family: "Font Awesome 5 Free";
        font-weight: 900;
    }
    </style>
    """, unsafe_allow_html=True)
