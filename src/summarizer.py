from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from src.prompts import get_summarizer_prompt
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    api_key = os.getenv("GROQ_API_KEY")
)

prompt = get_summarizer_prompt()

def summarize_text(text: str) -> str:

    if not text or not text.strip():
        return "No text provided"
    
    try:
        chain = llm | prompt

        result = chain.invoke({"input": text})

        return result.content
    
    except Exception as e:
        print(f"Summarization error: {e}")
        return "Summary unavailable"
    

    
