import streamlit as st
from app import get_best_answer
st.title("🤖 FAQ Chatbot")

st.write("Ask any question from the FAQ dataset")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):

    if user_input:

        response = get_best_answer(user_input)

        st.success(response)