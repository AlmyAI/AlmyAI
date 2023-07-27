import streamlit as st
from class_SalesforceAssistant import SalesforcePreAssistant

message_assistant_initial = "Hi I am Almy - your personal autonomous AI assistant. How can I help you?"
message_placeholder_chatinput = "Create opportunity, get leads, etc..."

#Set initial message
if 'messages' not in st.session_state:
  st.session_state.messages = [{"role": "assistant", "content": message_assistant_initial}]

#Display initial message
for message in st.session_state.messages:
  st.chat_message(name = message['role']).write(message['content'])

#set chat input
userinput = st.chat_input(placeholder = message_placeholder_chatinput)

#action if a prompt is entered
if userinput:
  message_user_initial = {"role": "user", "content": userinput}
  st.session_state.messages.append(message_user_initial)
  st.chat_message(name = "user").write(userinput)

  sfAssistant = SalesforcePreAssistant()
  sfAssistantResponse = sfAssistant.get_SalesforcePreAssistant(userinput)
  message_assistant_response = {"role": "assistant", "content": sfAssistantResponse}
  st.session_state.messages.append(message_assistant_response)
  st.chat_message(name = "assistant").write(sfAssistantResponse)
