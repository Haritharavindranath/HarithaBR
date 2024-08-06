from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')

print(f"Google API Key: {google_api_key}")
print(f"Serper API Key: {serper_api_key}")


