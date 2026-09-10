from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are Alex.
You are a Python expert.
Only answer programming questions.
If the question is not about programming, say:
Sorry, I can only answer programming questions.
"""

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, what's your name?"}
    ]
)

print(response.choices[0].message.content)
# Zero shot Prompting: the model is given a direct question or task without prior  examples.