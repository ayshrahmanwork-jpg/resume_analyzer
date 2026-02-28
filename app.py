import streamlit as st
import PyPDF2
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-2.5-flash")

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (PDF) and get AI-powered feedback.")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def analyze_with_ai(resume_text):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
You are an expert resume reviewer.

Analyze the following resume and provide:

1. Overall evaluation
2. Key strengths
3. Weaknesses
4. Specific improvement suggestions

Resume:
{resume_text[:4000]}
"""

    response = model.generate_content(prompt)
    return response.text


# ================= MAIN =================

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📌 Resume Preview")
    st.text(resume_text[:1000])

    if st.button("🚀 Analyze with AI"):
        with st.spinner("AI is analyzing your resume..."):
            ai_feedback = analyze_with_ai(resume_text)

        st.subheader("🤖 AI Feedback")
        st.write(ai_feedback)