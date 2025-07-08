import streamlit as st
import fitz  # from pymupdf
import requests
import json

# ========== Gemini API Setup ==========
API_KEY = "Use your api key here "
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
HEADERS = {
    "Content-Type": "application/json"
}


# ========== Function: Extract Resume Text ==========
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# ========== Function: Generate Questions via Gemini ==========
def generate_questions_from_resume(resume_text):
    prompt = f"""
You are an AI interviewer.
Read this resume text and generate:
- 10 technical interview questions based on detected skills
- 5 HR questions
- 3 scenario-based questions

Resume:
\"\"\"
{resume_text}
\"\"\"

Format your response like:
TECHNICAL QUESTIONS:
1. ...
2. ...
...
HR QUESTIONS:
1. ...
...
SCENARIO-BASED QUESTIONS:
1. ...
...
    """

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={API_KEY}",
        headers=HEADERS,
        data=json.dumps(body)
    )

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"⚠️ Failed to parse Gemini response: {e}"
    else:
        return f"❌ Gemini API Error: {response.status_code} - {response.text}"


# ========== Streamlit Dashboard ==========
st.set_page_config(page_title="AI Interview Question Generator", layout="centered")
st.title("🤖 Gemini Resume Interview Question Generator")
st.markdown("Upload your resume and get **AI-generated interview questions** in seconds!")

uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF Only)", type=["pdf"])

if uploaded_file:
    with st.spinner("⏳ Extracting resume and contacting Gemini AI..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        result = generate_questions_from_resume(resume_text)

    st.success("✅ Questions Generated!")
    st.text_area("📌 AI-Generated Questions", value=result, height=500)

else:
    st.info("👆 Please upload a PDF resume to continue.")
