import os
from openai import OpenAI

def generate_summary(text):
    """
    Generates exam-focused study notes from PDF text
    
    Args:
        text: Extracted PDF text
        
    Returns:
        str: Clean, structured summary
    """
    # Get API key (should already be loaded in app.py)
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        return "❌ Error: OPENROUTER_API_KEY not found. Please check your .env file."
    
    # Initialize OpenAI client for OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    # Create prompt for summary
    prompt = f"""
    You are an expert study notes creator. Analyze the following educational content and create clear, exam-focused study notes.
    
    Requirements:
    - Organize information into clear sections with headings
    - Highlight key concepts and definitions
    - Include important points and examples
    - Make it easy to review for exams
    - Use bullet points where appropriate
    - Keep language clear and concise
    
    Content to summarize:
    {text[:8000]}
    
    Generate comprehensive study notes:
    """
    
    # Try multiple free models as fallback
    models = [
        "google/gemini-flash-1.5",
        "meta-llama/llama-3.2-3b-instruct:free",
        "mistralai/mistral-7b-instruct:free"
    ]
    
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            # If this was the last model, return error
            if model == models[-1]:
                return f"❌ Error: All models failed. Last error: {str(e)}\n\nTip: The free tier might be rate-limited. Try again in a few minutes or add your own API key at OpenRouter."
            # Otherwise, try next model
            continue