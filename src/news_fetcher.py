import requests
import os

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsdata.io/api/1/news"

categories = ["business", "politics", "entertainment", "sports", "technology"]

def fetch_news(max_articles=4):
    """This function fetches news articles from newsdata.io API."""

    all_news = {} 

    for category in categories:
        params = {
            "apikey": API_KEY,
            "category": category,
            "language": "en",
            "country": "in"
        }

        res = requests.get(BASE_URL, params=params)

        data = res.json().get("results", [])

        articles = [] 

        for item in data[:max_articles]:
            articles.append({
                "title": item.get("title"),
                "url": item.get("link"),
                "source": item.get("source_id")
            })

        all_news[category] = articles

    return all_news




    



