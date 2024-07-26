import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
import warnings

# Suppress warnings
def faq():
    warnings.filterwarnings("ignore")

# Initialize the Google Generative AI model
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyCUy3AB6ywc11Kkf8VG7M64m7Svfky7qxs", temperature=0.5)

    # Function to ask a question and get an answer
    def ask_question(question):
        response = llm.generate(
            prompts=[question],
            max_tokens=100  # Adjust max_tokens as needed
        )
        print(response)
        # Access the generated text from the LLMResult
        answer = response.generations[0][0].text
        return answer

    # Streamlit page setup
    st.title("FAQ Page")

    # Input field for user questions
    question = st.text_input("Ask a question:")

    # Button to submit the question
    if st.button("Ask"):
        if question:
            # Get the answer from the model
            answer = ask_question(question)
            st.subheader("Answer:")
            st.write(answer.strip())
        else:
            st.warning("Please enter a question before clicking 'Ask'.")
