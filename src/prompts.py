from langchain_core.prompts import ChatPromptTemplate


def get_summarizer_prompt():
    """This function returns a prompt template for summarizing news articles."""

    system = """
You are a professional news editor.
Your task is to: Summarize news articles clearly, accurately, and neutrally in 3 to 4 lines.

**RULES:**
- Write in a factual news-reporting tone.
- Do not add opinions, assumptions, or information not present in the article.
- Use clear, professional news language.
- Focus only on key facts and events.
"""


    human = """
Summarize the following news article: 

ARTICLE TEXT:

{input}
"""


    return ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", human)
    ])