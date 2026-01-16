import boto3
import json
import os

from dotenv import load_dotenv
load_dotenv()

class S3Uploader:
    def __init__(self):
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )

    
    def upload_json(self, data, filename = "news_data.jsom"):

        try:

            json_data = json.dumps(data)

            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=filename, 
                Body=json.dumps(data),
                ContentType="application/json"
            )

            return True
        
        except Exception as e:
            print(f"Error uploading to S3: {e}")

            return False
        

    def download_json(self, filename="news_data.json"):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=filename)
            content = response["Body"].read().decode("utf-8")
            return json.loads(content)

        except Exception as e:
            print(f"Error downloading from S3: {e}")
            return None