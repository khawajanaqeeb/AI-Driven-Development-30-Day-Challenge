import os
from openai import OpenAI

def generate_quiz(text):
    """
    Generates MCQs and short questions from PDF text
    
    Args:
        text: Extracted PDF text
        
    Returns:
        str: Formatted quiz with MCQs and short questions
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
    
    # Create prompt for quiz generation
    prompt = f"""
    You are an expert exam question creator. Based on the following educational content, create a quiz with:
    
    1. **5 Multiple Choice Questions (MCQs)**
       - Each question should have 4 options (A, B, C, D)
       - Mark the correct answer clearly with ✓
       - Cover different topics from the content
       - Make questions challenging but fair
    
    2. **5 Short Answer Questions**
       - Questions that require 2-3 sentence answers
       - Test understanding of key concepts
       - Focus on application and comprehension
    
    Format your response EXACTLY like this:
    
    ═══════════════════════════════════════
    📝 MULTIPLE CHOICE QUESTIONS
    ═══════════════════════════════════════
    
    Q1. [Question text here]
    A) [Option A]
    B) [Option B]
    C) [Option C]
    D) [Option D]
    ✓ Correct Answer: [Letter]
    
    Q2. [Question text here]
    A) [Option A]
    B) [Option B]
    C) [Option C]
    D) [Option D]
    ✓ Correct Answer: [Letter]
    
    [Continue for all 5 MCQs]
    
    ═══════════════════════════════════════
    ❓ SHORT ANSWER QUESTIONS
    ═══════════════════════════════════════
    
    Q1. [Question text]
    
    Q2. [Question text]
    
    Q3. [Question text]
    
    Q4. [Question text]
    
    Q5. [Question text]
    
    Content to create quiz from:
    {text[:8000]}
    
    Generate the quiz now:
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
                temperature=0.8,
                max_tokens=2500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            # If this was the last model, return error
            if model == models[-1]:
                return f"❌ Error: All models failed. Last error: {str(e)}\n\nTip: The free tier might be rate-limited. Try again in a few minutes or add your own API key at OpenRouter."
            # Otherwise, try next model
            continue