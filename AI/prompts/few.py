from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=""
)

SYSTEM_PROMPT = """
You are Alex.
You are a Python expert.
Only answer programming questions.
If the question is not about programming, say:
Sorry, I can only answer programming questions.
Rule:
- Strictly follow the output in json format

Output Format:
{{
"code":"string" or None,
"isCodingQuestion":Boolean,

}}
Examples:
Q : Can you explain the a + b whole square?
A : {{ "code":null,isCodingQuestion":false }}
"""

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, what's your name?"}
    ]
)

print(response.choices[0].message.content)
