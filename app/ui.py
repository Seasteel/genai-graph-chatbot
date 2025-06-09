import streamlit as st
from chatbot import ask_graph

st.title("Gen AI Graph Chatbot")

user_input = st.text_input("Таны асуулт:")
if st.button("Асуух"):
    if user_input:
        answer = ask_graph(user_input)
        st.write(answer)
