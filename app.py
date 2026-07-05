import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 FAQ Chatbot")
st.write("👋 Welcome to the FAQ Chatbot!")
st.write("Ask a question related to Python, AI, GitHub, HTML, CSS, SQL, and more.")

questions = [
    "What is Python?",
    "What is AI?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Streamlit?",
    "What is GitHub?",
    "What is Data Science?",
    "What is NLP?",
    "What is a Chatbot?",
    "What is Programming?",
    "What is HTML?",
    "What is CSS?",
    "What is JavaScript?",
    "What is SQL?",
    "What is an API?"
]

answers = [
    "Python is a popular programming language used for web development, AI, and data science.",
    "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "Machine Learning is a branch of AI where computers learn from data without being explicitly programmed.",
    "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",
    "Streamlit is a Python library used to build interactive web applications quickly.",
    "GitHub is a platform used to store, manage, and share source code using Git.",
    "Data Science is the process of analyzing data to extract useful insights.",
    "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "A chatbot is a software application that can communicate with users using text or voice.",
    "Programming is the process of writing instructions for computers.",
    "HTML is the standard markup language used to create web pages.",
    "CSS is used to style and design web pages.",
    "JavaScript is a programming language used to make websites interactive.",
    "SQL is a language used to manage and query databases.",
    "An API (Application Programming Interface) allows different software applications to communicate with each other."
]

user_question = st.text_input("Ask your question")

if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(questions + [user_question])

        similarity = cosine_similarity(vectors[-1], vectors[:-1])
        index = similarity.argmax()

        score = similarity[0][index]

        if score > 0.3:
            st.success(answers[index])
        else:
            st.error("❌ Sorry, I don't know the answer to that question.")