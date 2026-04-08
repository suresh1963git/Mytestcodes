import streamlit as st

st.set_page_config(page_title="India Quiz App", page_icon="📝", layout="centered")

st.title("📝 Question Answer Session")
st.write("Select the correct answer for each question and click **Submit** to see your score.")

# Questions and answers
questions = [
    {
        "question": "1. Capital of Tamil Nadu",
        "options": ["Chennai", "Madurai", "Coimbatore", "Trichy"],
        "answer": "Chennai"
    },
    {
        "question": "2. Capital of India",
        "options": ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "3. Prime Minister of India",
        "options": ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Yogi Adityanath"],
        "answer": "Narendra Modi"
    },
    {
        "question": "4. National Animal of India",
        "options": ["Lion", "Elephant", "Tiger", "Leopard"],
        "answer": "Tiger"
    },
    {
        "question": "5. National Bird of India",
        "options": ["Parrot", "Peacock", "Sparrow", "Crow"],
        "answer": "Peacock"
    }
]

# Store user answers
user_answers = []

for i, q in enumerate(questions):
    selected_option = st.radio(
        q["question"],
        q["options"],
        key=f"q{i}"
    )
    user_answers.append(selected_option)

# Submit button
if st.button("Submit"):
    score = 0

    st.subheader("Results")
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
            st.success(f"{q['question']} - Correct ✅")
        else:
            st.error(
                f"{q['question']} - Wrong ❌ | Correct Answer: {q['answer']}"
            )

    st.subheader(f"Your Total Score: {score} / {len(questions)}")
    st.info(f"Marks Obtained: {score}")