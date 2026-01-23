from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from src.prompts import get_summarizer_prompt

llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    api_key = os.getenv("GROQ_API_KEY")
)

prompt = get_summarizer_prompt()

def summarize_text(text: str) -> str:

    if not text:
        return "No text"
    
    try:
        chain = llm | prompt

        result = chain.invoke({"input": text})

        return result.content
    except Exception:
        return "No Summary available"
    

    
