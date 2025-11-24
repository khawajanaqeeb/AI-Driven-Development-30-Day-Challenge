from PyPDF2 import PdfReader
import streamlit as st

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from uploaded PDF file
    
    Args:
        pdf_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text from all pages
    """
    try:
        # Create PDF reader object
        pdf_reader = PdfReader(pdf_file)
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text
    
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None