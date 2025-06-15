# 🎓 MCQ Generator using Generative AI

This project utilizes the OpenAI API and LangChain to create a Generative AI model that generates multiple-choice questions (MCQs) based on given input files. The model accepts `.txt` and `.pdf` files and allows users to specify the subject and tone (difficulty level) to generate the desired number of MCQs. An engaging web interface is built using Streamlit for easy interaction.

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](https://example.com)

In this project, we have leveraged the capabilities of OpenAI models and Langchain API to generate quiz questions of MCQ or True/False type from a given text/PDF. The project aims to automate the process of generating quiz questions, thereby saving time and effort for educators, content creators, and learners. By utilizing advanced natural language processing (NLP) models, the application can extract key information from the text and formulate relevant quiz questions based on the content.

The user can decide the number of questions to be generated, and the complexity level of the questions. The application provides a user-friendly interface that allows users to input the text or upload a PDF document, select the desired parameters, and generate quiz questions with a single click. The generated questions can be used for educational purposes, training materials, assessments, or content creation across various domains.

## 🚀 Setup and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aashay30/MCQ_Generator
   cd mcq-generator

2. **Create a virtual environment**:
   ```bash
   conda create --name env python=3.9

3. **Activate the environment**:
   ```bash
   conda activate env

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

5. **Set up your OpenAI API key**:
    Make sure to set your OpenAI API key in your environment variables. You can do this by adding the following line to your .bashrc or .bash_profile:

   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
    ```

   Replace 'your_openai_api_key' with your actual OpenAI API key

6. **Run the Streamlit app**:
   ```bash
   streamlit run app.py


The web interface should open in your browser automatically. If it doesn't, the local URL will be output in the terminal; just copy it and open it manually. By default, it will be http://localhost:8501/.

## 📄 Data Input

The model accepts input files in the following formats:

- **Text files (`.txt`)**
- **PDF files (`.pdf`)**

You can upload these files through the web interface and specify the subject and tone to generate MCQs.

## 🎉 Features

- Generate MCQs based on provided input files.
- Specify the subject and tone (difficulty level) for tailored question generation.
- User-friendly interface built with Streamlit for easy interaction.

## 🌐 Web Interface

The web interface allows users to upload files, specify the subject, and set the difficulty level. Once the input is provided, the model generates the desired number of MCQs, which can be viewed and downloaded.

Feel free to explore the project and enhance the MCQ generation experience! 📚✨
