import requests
import os


EXTRACTOR_API_KEY = os.getenv("EXTRACTOR_API_KEY")


def get_full_text(url):
    """This function fetches full text from url. """

    if not EXTRACTOR_API_KEY:
        print("EXTRACTOR API KEY not found")
        return None

    try:
        response = requests.get(
            "https://extractorapi.com/api/v1/extractor",
            params={
                "apikey": EXTRACTOR_API_KEY,
                "url": url
            },
            timeout=15
        )

        if response.status_code != 200:
            print(f"Extractor API error: {response.status_code}")
            return None
        
        data = response.json()

        return data.get("text", None)
    
    except Exception as e:
        print(f"Extractor API error: {e}")
        return None