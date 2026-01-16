import os 
import requests
from dotenv import load_dotenv
load_dotenv()

class TextExtractor:
    """This class is responsible for extracting text from a given URL"""

    def __init__(self):
        self.base_url = "https://extractorapi.com/api/v1/extractor"
        self.api_key = os.getenv("EXTRACTOR_API_KEY")


    def extract_text(self, url):
        """This function accepts a URL and uses EXTRACTOR API to extract text from it"""

        try:
            
            response = requests.get(
                self.base_url,
                params = {
                    "url" : url,
                    "apikey" : self.api_key
                }, timeout = 15
            )

            data = response.json()

            return data.get("text", None)
        
        except Exception as e:
            print(e)

            return None