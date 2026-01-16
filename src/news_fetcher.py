import os
from dotenv import load_dotenv
load_dotenv()

import requests


class NewsFetcher:
    """This class is responsible for fetching news articles from GNews API"""

    def __init__(self):
        self.api_key = os.getenv("GNEWS_API_KEY")
        self.base_url = "https://gnews.io/api/v4/top-headlines"
        self.categories = ["business", "technology", "entertainment", "sports", "nation"]


    def fetch_articles(self, max_articles = 4):
        """Get articles from GNews API"""
        
        all_articles = []

        for category in self.categories:

            try:

                params = {
                    "category": category ,
                    "lang": "en",
                    "country": "in",
                    "max": max_articles,
                    "apikey": self.api_key
                }

                response = requests.get(self.base_url, params=params)

                if response.status_code != 200:
                    continue

                data = response.json().get("articles", [])



                for art in data:
                    all_articles.append(
                        {
                            "title": art.get("title"),
                            "url": art.get("url"),
                            "source": art.get("source", {}).get("name", "Unknown"),
                        }
                    )


            except Exception as e:
                raise RuntimeError(f"Error fetching news: {e}")


        return all_articles