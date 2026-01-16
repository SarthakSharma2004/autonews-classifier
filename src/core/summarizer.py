from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.prompt.summarizer_prompt import get_summarizer_prompt
import os 
from dotenv import load_dotenv
load_dotenv()


class SummarizeNews:
    """
    This class is responsible for summarizing the text of a news article
    """

    def __init__(self):

        self.llm = ChatGroq(model = "qwen/qwen3-32b", api_key = os.getenv("GROQ_API_KEY"))
        self.prompt = get_summarizer_prompt()
        self.chain = self.prompt | self.llm



    def summarize_article(self, text: str) -> str:
        """Generate Summary"""

        try:

            response = self.chain.invoke({"input": text})

            return response.content

        except Exception as e:
            print(e)

            return "Could not generate summary"

        