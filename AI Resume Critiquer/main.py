import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ui code

st.set_page_config(
    page_title="AI Resume Critiquer",
    page_icon="📄",
    layout="centered"
)

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

uploaded_file = st.file_uploader(
    "Upload your resume here (PDF or TXT):",
    type=["pdf", "txt"]
)

job_role = st.text_input(
    "Enter the job role you are targeting (optional):"
)

analyze = st.button("Analyze Resume")


def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    else:
        return uploaded_file.read().decode("utf-8", errors="ignore")


# main logic
if analyze and uploaded_file:
    try:
        # Check API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("OPENAI_API_KEY not found. Please set it in your environment.")
            st.stop()

        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file does not contain readable text.")
            st.stop()

        # Limit input size 
        MAX_CHARS = 6000
        file_content = file_content[:MAX_CHARS]

        role_text = job_role if job_role else "general job applications"

        prompt = f"""
You are an expert resume reviewer.

Analyze the following resume and provide constructive feedback focused on:
1. Content clarity and impact
2. Skills presentation
3. Experience descriptions
4. Improvements specific to {role_text}

Resume content:
{file_content}

Provide your feedback in a clear, structured format with actionable recommendations.
"""

        client = OpenAI(api_key=api_key)

        with st.spinner("Analyzing resume..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt,
                temperature=0.7,
                max_output_tokens=800
            )

        st.markdown("### 📊 Analysis Results")
        st.markdown(response.output_text)

    except Exception as e:
        st.error(f"There was an error: {str(e)}")
