import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file , get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain # need parameter
from src.mcqgenerator.logger import logging

# loading the json file
with open("G:\Generative AI\MCQ Generator\Automated-MCQ-Generator-Using-Langchain-OpenAI-API-main\Response.json" , 'r') as file:
    RESPONSE_JSON = json.load(file)
    
# creating title for the app
st.title("MCQs Generator Application with LangChain")

# creating a form
with st.form("user_inputs"):
    
    # file upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")
    
    # input feilds
    mcq_count = st.number_input("Number of MCQs to be generated" , min_value=3 , max_value=50)
    
    # subject 
    subject = st.text_input("Input Subject" , max_chars=20)
    
    # quiz_tone : can be simple , intermediate , hard
    tone = st.text_input("Complexity level of Questions" , max_chars=20 , placeholder='simple')
    
    # add button
    button = st.form_submit_button("Generate MCQs")
    
    # check if button is clicked and all feilds have input
    if button and uploaded_file and mcq_count and subject and tone is not None :
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                
                # count tokens and cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text" : text,
                            "number" : mcq_count,
                            "subject" : subject,
                            "tone" : tone,
                            "response_json" : json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e) , e, e.__traceback__)
                st.error("Error")
                
            else:
                print(f"Total Tokens : {cb.total_tokens}")
                print(f"Prompt Tokens : {cb.prompt_tokens}")
                print(f"Compeltion Tokens : {cb.completion_tokens}")
                print(f"Total Cost : {cb.total_cost}")
                
                if isinstance(response , dict):
                    
                    # extract the quiz data from the response
                    
                    quiz = response.get("quiz" , None)
                    
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            
                            # display reveiw in tex box
                            st.text_area(label="Reveiw" , value=response["reveiw"])
                            
                        else:
                            st.error("Error in the table data")
                            
                    else:
                        st.write(response)
                        
                        
                    