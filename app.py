import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (PDF) and get feedback.")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📌 Resume Preview")
    st.text(resume_text[:1000])

    # Simple keyword check
    keywords = ["python", "machine learning", "data", "project", "sql"]
    found = [word for word in keywords if word.lower() in resume_text.lower()]

    st.subheader("✅ Keywords Found")
    st.write(found if found else "No important keywords found")

    st.subheader("💡 Suggestions")

    if len(found) < 3:
        st.warning("Add more technical keywords to strengthen your resume.")
    else:
        st.success("Good keyword coverage!")