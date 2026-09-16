from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

load_dotenv()

client = OpenAI()


def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C%t"
    response = requests.get(url)

    return response.text


def main():

    user_query = input("> ")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get weather of a city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string"
                            }
                        },
                        "required": ["city"]
                    }
                }
            }
        ]
    )

    message = response.choices[0].message

    # AI wants to use weather function
    if message.tool_calls:

        tool_call = message.tool_calls[0]

        city = json.loads(
            tool_call.function.arguments
        )["city"]

        result = get_weather(city)

        print(result)
    else:
        print(message.content)


main()