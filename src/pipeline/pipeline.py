from datetime import datetime
from core.news_fetcher import NewsFetcher
from extractor import TextExtractor
from classifier import Classifier
from core.summarizer import SummarizeNews

import json

class Orchestrator:
    """Orchestrator class for the pipeline"""

    def __init__(self):
        self.fetcher = NewsFetcher()
        self.extractor = TextExtractor()
        self.classifier = Classifier()
        self.summarizer = SummarizeNews()

    
    def run_pipeline(self):
        """This function orchestrates the entire pipeline"""

        results = []

        articles = self.fetcher.fetch_articles()

        for art in articles:
            title = art['title']
            url = art['url']
            source = art['source']

            full_text = self.extractor.extract_text(url)

            if not full_text :
                continue

            try:
                predicted_label = self.classifier.predict(full_text)

            except Exception as e:
                continue

            summary = self.summarizer.summarize_article(full_text)  

            results.append(
                {
                    "title": title,
                    "url": url,
                    "source": source,
                    "predicted_label": predicted_label,
                    "summary": summary,
                    "date": datetime.now().isoformat()
                }
            ) 

        self.save_to_json(results)
        return results

    def save_to_json(self, data):
        with open("news_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Saved {len(data)} articles to news_data.json")

    
if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run_pipeline()