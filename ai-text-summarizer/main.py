from urllib import response

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
text = input("Enter text to summarize:\n\n")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"summarize the following text in 5-6 line:\n\n {text}",
)
print("\nSummary:\n")
print(response.text)