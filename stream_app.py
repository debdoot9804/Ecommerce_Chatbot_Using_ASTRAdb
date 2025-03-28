import streamlit as st
from dotenv import load_dotenv
from ecomm.retrieval import generate
from ecomm.ingest import ingest_data

load_dotenv()

# Initialize Chain only once
@st.cache_resource
def load_chain():
    v_store = ingest_data("Data Already Uploaded to AstraDB")
    chain = generate(v_store)
    return chain

chain = load_chain()

st.set_page_config(page_title="🛒 Ecommerce_Laptop Chatbot", page_icon="🤖")
st.title("🛒 E-Commerce Ecommerce_Laptop Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if query := st.chat_input("How can I help you..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Get bot response
    with st.chat_message("assistant"):
        
            result = chain.invoke(query)
            st.markdown(result)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": result})
