import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerationModel, Part, Content, ChatSession

project = "sample-gemini"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

model = GenerationModel(
    "gemini-pro",
    generation_config = config
)
chat = model.start_chat()

# helper func to display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    with st.chat_message("model"):
        st.markdown(output)
        
    st.session_state.message.append(
        {
            "role": "user",
            "content":query
        }
    )
    
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )
    
st.title("Gemini Explorer")

# initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#display and load chat history
for index, messages in enumerate(st.session_state.messages):
    content = Content(
            role = messages["role"],
            parts = [Part.from_text(messages["content"]) ]
        )
    
    if index !=0:
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])
            
    chat.history.append(content)


#for initial message startup
if len(st.session_state.messages) == 0:
    initial_message = "Welcome to Gemini Explorer! How can I assist you today?"

#for capture user input 
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)