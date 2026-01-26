import requests
import os

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsdata.io/api/1/news"

categories = ["business", "politics", "entertainment", "sports", "technology"]

def fetch_news(max_articles=4):
    """This function fetches news articles from newsdata.io API."""
    
    if not API_KEY:
        print("API KEY not found")
        return {}
    
    all_news = {} 

    for category in categories:
        try: 
            params = {
                "apikey": API_KEY,
                "category": category,
                "language": "en",
                "country": "in"
            }

            res = requests.get(BASE_URL, params=params, timeout=10)

            if res.status_code != 200:
                print(f"Error fetching news for category {category}: {res.status_code}")
                continue

            data = res.json().get("results", [])

            
            articles = [] 

            for item in data[:max_articles]:

                articles.append({
                    "title": item.get("title"),
                    "url": item.get("link"),
                    "source": item.get("source_id")
                })

            all_news[category] = articles

        except Exception as e:
            print(f"Error fetching news for category {category}: {e}")
            continue

    return all_news




    



