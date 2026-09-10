#chain of Thought Prompting


from openai import OpenAI
import os
from dotenv import load_dotenv
import json

from openai.types.beta.threads import message

from AI.hello_world.main import response

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """
You're an expert AI Assistant In resolving user queries using chain of thought.
You Work on START,PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps
Once you think  enough PLAN has be done, finally you can give OUTPUT.

Rules:
 - Strictly Follow the given JSON output Format
 - Only run one step at a time.
 - the sequence of steps is START (where user given an input),plan (That can be multiple times) and finally OUTPUT(which is going to the user).
 
 
 Output JSON Format:
 { "step":"START" | "PLAN" | "OUTPUT" , "content" : "string" }
 
 
 Example:
 START :  Hey, Can You solve 2 + 3 * 5 / 10
 PLAN:
{
    "step": "PLAN",
    "content": "Identify the mathematical expression and determine the correct order of operations."
}

PLAN:
{
    "step": "PLAN",
    "content": "Apply BODMAS: multiplication and division are performed before addition."
}

PLAN:
{
    "step": "PLAN",
    "content": "Calculate 3 * 5 = 15, then 15 / 10 = 1.5, and finally 2 + 1.5 = 3.5."
}

OUTPUT:
{
    "step": "OUTPUT",
    "content": "The answer is 3.5."
}

"""


message_history = [{
    "role":"system","content":SYSTEM_PROMPT
}]
user_query = input("-> ")
message_history.append({"role":"user","content":user_query})
while True:
    response = client.chat.completions.create(
        model="gemini-3.6-flash",
        messages=message_history
    )
    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant","content":raw_result})
    parsed_result = json.loads(raw_result)
    if parsed_result["step"] == "START":
        print("STARTing LLM LOOP",parsed_result.get("content"))
        continue

    if parsed_result["step"] == "PLAN":
        print("PLAN",parsed_result.get("content"))


    if parsed_result["step"] == "OUTPUT":
        print("OUTPUT",parsed_result.get("content"))
        break




# response = client.chat.completions.create(
#     model="gemini-3.6-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": SYSTEM_PROMPT
#         },
#         {
#             "role": "user",
#             "content": "Hey, write code to add n numbers in JavaScript"
#         }
#     ]
# )
#
# print(response.choices[0].message.content)
#
# print(response.choices[0].message.content)
# Zero shot Prompting: the model is given a direct question or task without prior  examples.

