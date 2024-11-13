import streamlit as st
import requests
from groq import Groq
import os
os.system("pip install groq")
# Streamlit app setup
st.title("Sifra AI")
st.write("Upload a text file to set the context for the chat. Enter your questions to get responses based on the content of the file.")

# Function to call Groq LLM API
def get_llm_response(question, context):
    
    client = Groq(
        api_key='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',
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                
                "role": "system",
                "content": "I will give you conversations with a person and a final question in the end. Capture his/her personality and respond to the final question only like him/her. Don't write anything else just write answer as if that same person is answering. Most importantly, Dont repeat at any condition. Just end the statement if repetation happens. ",
            
            },
            {
                "role": "user",
                "content": context+"\n\n Final Question: How do you handle depression?",
            }
        ],
        model="llama-3.2-90b-vision-preview",
    )

    return (chat_completion.choices[0].message.content)

# File upload
# if ()
uploaded_file = st.file_uploader("Upload a text file", type="txt")
if uploaded_file:
    # Reading the uploaded text file content
    context = uploaded_file.read().decode("utf-8")
    
    # Chat interface
    st.write("### Chat")
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You: ", key="input")
    
    if st.button("Send"):
        if user_input:
            # Display user's question in the chat
            st.session_state.conversation.append(("You", user_input))
            
            # Get response from LLM
            response = get_llm_response(user_input, context)
            if response:
                # Display LLM's response in the chat
                st.session_state.conversation.clear()
                st.session_state.conversation.append(("AI", response))
                
                
            # Clear user input
            st.session_state.inputs = ""

    # Display conversation history
    for speaker, message in st.session_state.conversation:
        st.write(f"**{speaker}**: {message}")

