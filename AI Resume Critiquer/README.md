## AI Resume Critiquer

An AI-powered web application built with Streamlit that analyzes resumes and provides structured, actionable feedback tailored to a target job role using a large language model.

Users can upload resumes in PDF or TXT format and receive personalized improvement suggestions in seconds.

# Features

Upload resumes in PDF or TXT format

Automatic text extraction from PDF files

AI-generated feedback on:

Content clarity and impact

Skills presentation

Experience descriptions

Role-specific improvements

Optional target job role input for tailored feedback

Clean and intuitive Streamlit interface

Secure API key handling via environment variables

# How It Works

The user uploads a resume (PDF or TXT).

The app extracts readable text from the file.

The user optionally specifies a target job role.

The resume content is sent to a large language model with a structured prompt.

The model returns detailed, actionable feedback.

Results are displayed directly in the web interface.

# Technologies Used

Python

Streamlit – Web application framework

PyPDF2 – PDF text extraction

OpenAI API – Large language model inference

python-dotenv – Environment variable management

# Installation

Clone the repository:

git clone https://github.com/your-username/ai-resume-critiquer.git
cd ai-resume-critiquer


Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

# Environment Setup

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here


# Running the App
streamlit run app.py


Open the provided local URL in your browser to use the application.

# Project Structure
ai-resume-critiquer/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .gitignore          # Git ignore rules

# Limitations

Feedback quality depends on the clarity of the uploaded resume

PDF text extraction may be imperfect for heavily formatted resumes

Large resumes are truncated to stay within model input limits

Not intended for production or professional hiring decisions

#  Possible Improvements

Resume scoring (per section)

ATS keyword matching

Job description upload and comparison

Export feedback as PDF

Multi-resume comparison

User authentication

# License

This project is intended for educational and portfolio use.

# Author

Developed by Nathan Pereira
Computer Science student with interests in AI, Robotics, and Gaming
