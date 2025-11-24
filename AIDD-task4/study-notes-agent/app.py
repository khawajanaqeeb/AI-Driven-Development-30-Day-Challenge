from dotenv import load_dotenv
import os

# Load environment variables FIRST before anything else
load_dotenv()

# Debug: Check if key is loaded
if not os.getenv("OPENROUTER_API_KEY"):
    import streamlit as st
    st.error("⚠️ OPENROUTER_API_KEY not found in .env file!")
    st.stop()

import streamlit as st
from utils.pdf_handler import extract_text_from_pdf
from agents.summary_agent import generate_summary
from agents.quiz_agent import generate_quiz

# Page configuration
st.set_page_config(
    page_title="Study Notes & Quiz Generator",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 Study Notes Summarizer & Quiz Generator")
st.markdown("Upload your study material and get AI-generated notes and quizzes!")

# Sidebar for file upload
with st.sidebar:
    st.header("📄 Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload your study material in PDF format"
    )

# Main content area
if uploaded_file is not None:
    # Extract text from PDF
    with st.spinner("📖 Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    
    if pdf_text:
        st.success("✅ PDF loaded successfully!")
        
        # Show extracted text preview (optional)
        with st.expander("📄 View Extracted Text Preview"):
            st.text(pdf_text[:500] + "..." if len(pdf_text) > 500 else pdf_text)
        
        # Create two tabs
        tab1, tab2 = st.tabs(["📝 Summary", "❓ Quiz"])
        
        # Summary Tab
        with tab1:
            st.header("Study Notes Summary")
            
            if st.button("Generate Summary", type="primary", key="summary_btn"):
                with st.spinner("🤖 Generating study notes..."):
                    summary = generate_summary(pdf_text)
                
                st.markdown("### Your Study Notes:")
                st.markdown(summary)
                
                # Download button
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="study_notes.txt",
                    mime="text/plain"
                )
        
        # Quiz Tab
        with tab2:
            st.header("Practice Quiz")
            
            if st.button("Generate Quiz", type="primary", key="quiz_btn"):
                with st.spinner("🤖 Creating quiz questions..."):
                    quiz = generate_quiz(pdf_text)
                
                st.markdown("### Your Quiz:")
                st.markdown(quiz)
                
                # Download button
                st.download_button(
                    label="📥 Download Quiz",
                    data=quiz,
                    file_name="practice_quiz.txt",
                    mime="text/plain"
                )
    
    else:
        st.error("❌ Failed to extract text from PDF. Please try another file.")

else:
    # Show instructions when no file is uploaded
    st.info("👈 Please upload a PDF file from the sidebar to get started!")
    
    st.markdown("""
    ### How to use:
    1. Upload your study material (PDF) using the sidebar
    2. Choose **Summary** tab to get exam-focused notes
    3. Choose **Quiz** tab to generate practice questions
    4. Download your notes and quiz for offline study
    
    ### Features:
    - ✨ AI-powered study notes generation
    - 📝 5 MCQs with 4 options each
    - ❓ 5 short answer questions
    - 💾 Download notes and quizzes
    """)