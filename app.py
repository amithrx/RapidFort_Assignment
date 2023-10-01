import streamlit as st
import requests

# App title
st.set_page_config(page_title="🦚🛐💬 GitaGPT 2.0")
# Define the URL of the backend API
backend_url = "http://127.0.0.1:5000/getResponse"
# Replicate Credentials
with st.sidebar:
    st.title('🦚🛐💬 GitaGPT 2.0')

    # Refactored from https://github.com/a16z-infra/llama2-chatbot
    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B'], key='selected_model')
    
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)
    
    st.markdown('📖 Learn how to build this app in this (https://github.com/amithrx/RapidFort_Assignment)!')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    # string_dialogue = "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    # Prepare the user input for the backend
    prompt_input = prompt_input + " Give answer by quoting examples from Bhagawad Gita."
    data = {"text": prompt_input,"temperature": temperature,"top_p": top_p,"max_length": max_length}
    try:
        # Send a POST request to the backend
        response = requests.post(backend_url, json=data)

        if response.status_code == 200:
            generated_response = response.json()["response"]
            return generated_response
        else:
            return "Error occurred while generating the response."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# User-provided prompt
if prompt := st.chat_input("User"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

