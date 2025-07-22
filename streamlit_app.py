import os
import json
import tracebqack
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Loading the json file
with open('./config/workspace/Response.json', 'r') as f:
    RESPONSE_JSON = json.load(f)

# Create title for the application
st.title("MCQ Generator Application - Powered by LangChain⛓️")

# Create a form
with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a file (pdf/text)", type=["pdf", "txt"])

    # Input fields
    mcq_number = st.number_input("Number of MCQs", min_value=3, max_value=20)
    # Subject
    subject = st.text_input("Insert Subject", max_chars=25)
    # Quiz Tone
    tone = st.selectbox("Complexity level of questions", max_chars=20, placeholder="Simple")
    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check If the button is clicked and all field have input
    if button and uploaded_file is not None and mcq_number and subject and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text=read_file(uploaded_file)
                # Count tokens and cost of API call
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "numbers": mcq_number,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
                # st.write(response["quiz"])
            except Exception as e:
                tracebqack.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

    else:
        print(f"Total Tokens : {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost: ${cb.total_cost:.4f}")
        if isinstance(response, dict):
            # Extract quiz data from the response
            quiz=response.get("quiz", None)
            if quiz is not None:
                # Convert the quiz data to a DataFrame
                quiz_table_data=get_table_data(quiz)
                if quiz_table_data is not None:
                    # Display the quiz data in a table format
                    df=pd.DataFrame(quiz_table_data)
                    df.index=df.index + 1
                    st.table(df)
                    # Display the review in a text box as well
                    st.text_area(label="Quiz Review", value=response["review"])
                else:
                    st.error("Error in the table data")
            else:
                st.write(response)

