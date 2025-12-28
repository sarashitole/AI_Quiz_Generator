import streamlit as st
from quiz_generator import generate_quiz

st.set_page_config(page_title="AI Quiz Generator")

st.title("🧠 AI Quiz Generator")
st.write("Generate quiz questions using AI")

text = st.text_area(
    "Enter Topic or Study Material",
    height=200
)

num_questions = st.slider(
    "Number of Questions",
    1, 10, 5
)

if st.button("Generate Quiz"):
    if text.strip() == "":
        st.warning("Please enter text!")
    else:
        with st.spinner("Generating quiz..."):
            quiz = generate_quiz(text, num_questions)
        st.success("Quiz Generated!")
        st.text_area("Result", quiz, height=300)
