from langchain_core.prompts import ChatPromptTemplate


def get_summarizer_prompt():
    """This function returns a prompt template for summarizing news articles."""

    system = """
You are a professional news summarizer. Your job is to read news articles and produce clear, concise, and factual summaries.
You must not add opinions or hallucinate facts.
"""

    human = """
Summarize the following news article in 5 to 6 lines. 
Use professional, formal language and write in third person
Keep the summary neutral and informative.

ARTICLE TEXT:
{input}
"""


    return ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", human)
    ])