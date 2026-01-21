import streamlit as st
from jarvis import ask_jarvis, add_knowledge

st.set_page_config(page_title="Jarvis AI", page_icon="🤖")
st.title("🤖 Jarvis – AI Assistant")

st.subheader("📚 Add Knowledge")
knowledge = st.text_area("Enter enterprise knowledge")
if st.button("Store in Vector DB"):
    add_knowledge(knowledge)
    st.success("Knowledge stored successfully")

st.subheader("💬 Chat with Jarvis")
query = st.text_input("Ask Jarvis")

if st.button("Ask"):
    response = ask_jarvis(query)
    st.write("### 🤖 Jarvis says:")
    st.write(response)
