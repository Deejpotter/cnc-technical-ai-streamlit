import streamlit as st

# Create an instance of the ChatEngine class
# This will run the __init__ method in the ChatEngine class
from chat_engine import ChatEngine

chat_engine = ChatEngine()


# Function to manage chat state
@st.cache_resource
def manage_chat_state():
    return {"chat": []}


# Sidebar for conversations
st.sidebar.title("Conversations")
conversations = ["Conversation 1", "Conversation 2"]
selected_conversation = st.sidebar.selectbox("Select a conversation", conversations)

# Main chat area
st.title(f"Chat - {selected_conversation}")

# Get the chat state
chat_state = manage_chat_state()

# Text input for user message
user_message = st.text_input("Type your message here...")

# Send button
if st.button("Send"):
    # Process the user message through your ChatEngine
    bot_response = chat_engine.process_user_input(user_message)

    # Update chat state
    chat_state["chat"].append({"user": user_message, "bot": bot_response})

# Display chat history
st.write("Chat History:")
for chat in chat_state["chat"]:
    st.write(f"User: {chat['user']}")
    st.write(f"Bot: {chat['bot']}")
