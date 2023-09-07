import streamlit as st
from chat_engine import ChatEngine

# Initialize the ChatEngine
chat_engine = ChatEngine()


# Function to manage chat state using Streamlit's cache
@st.cache_resource
def manage_chat_state():
    # Initialize an empty chat state
    return {"chat": []}


# Sidebar for listing conversations
st.sidebar.title("Conversations")
conversations = ["Conversation 1", "Conversation 2"]
# Dropdown to select a conversation
selected_conversation = st.sidebar.selectbox("Select a conversation", conversations)

# Main chat area
st.title(f"Chat - {selected_conversation}")

# Retrieve the current chat state
chat_state = manage_chat_state()

# Create a placeholder for the text input
text_input_placeholder = st.empty()

# Text input for user message
# We use the placeholder to create the text input so that we can clear it later
user_message = text_input_placeholder.text_input("Type your message here...")

# Send button to submit the message
if st.button("Send"):
    # Process the user's message and get the bot's response
    bot_response = chat_engine.process_user_input(user_message)

    # Update the chat state with the new messages
    chat_state["chat"].append({"user": user_message, "bot": bot_response})

    # Clear the text input field by updating the placeholder
    text_input_placeholder.text_input("Type your message here...", value="", key="new_key_for_input")

# Display the chat history
st.write("## Chat History:")
for chat in chat_state["chat"]:
    # Display user's messages
    st.markdown(f"**You**: {chat['user']}")
    # Display bot's messages
    st.markdown(f"_Assistant_: {chat['bot']}")
