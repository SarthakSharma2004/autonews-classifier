import requests
import os


EXTRACTOR_API_KEY = os.getenv("EXTRACTOR_API_KEY")


def get_full_text(url):
    """This function fetches full text from url. """

    try:
        response = requests.get(
            "https://extractorapi.com/api/v1/extractor",
            params={
                "apikey": EXTRACTOR_API_KEY,
                "url": url
            },
            timeout=15
        )
        data = response.json()
        
        return data.get("text", None)
    except:
        return None