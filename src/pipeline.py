import json
from src.news_fetcher import fetch_news
from src.extractor import get_full_text
from src.classifier import predict_class
from src.summarizer import summarize_text
from dotenv import load_dotenv

load_dotenv()

def run_pipeline():

    final_output = []

    news = fetch_news()   # category → articles

    for category in news:
        for article in news[category]:

            url = article["url"]
            title = article["title"]
            source = article["source"]

            full_text = get_full_text(url)

            label = predict_class(full_text)
            
            summary = summarize_text(full_text)

            final_output.append({
                "title": title,
                "url": url,
                "source": source,
                "predicted_category": label,
                "summary": summary
            })

    # save for Streamlit
    with open("final_news.json", "w") as f:
        json.dump(final_output, f, indent=4)

    return final_output


if __name__ == "__main__":
    run_pipeline()
