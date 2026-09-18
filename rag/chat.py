from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

from openai import OpenAI


load_dotenv()

open_ai = OpenAI()
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333/",
    collection_name="learning_rag",
    embedding = embeddings_model,
)

# Take User Input
user_query =  input("Enter a query: ")

# Relevant Search
search_result = vector_db.similarity_search(query=user_query)
print(search_result)

context = "\n\n".join(
    f"# Page Content: {result.page_content}\n"
    f"Page Number: {result.metadata['page_label']}\n"
    f"File Location: {result.metadata['source']}"
    for result in search_result
)

SYSTEM_PROMPT = f"""
You are a helpful AI assistant. Answer the user's question only
using the context retrieved from the PDF.

If the answer is not in the context, say:
"I couldn't find the answer in the provided PDF."

Mention the relevant PDF page number so the user can check it.

Context:
{context}
"""

response = open_ai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query},
    ]
)
print(response)
# ChatCompletion(id='chatcmpl-EPQvZ6flHgzRw0tzWEh52zsjGSixo', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='A for loop in Python is used to iterate through a sequence like a list, tuple, or string (iterables). The syntax for a for loop is shown below:\n\n```python\nl = [1, 7, 8] \nfor item in l: \n    print(item) # prints 1, 7 and 8\n```\n\n(Page 27 of the PDF)', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1789730417, model='gpt-4o-2024-08-06', object='chat.completion', metadata=None, moderation=None, service_tier='default', system_fingerprint='fp_d77fe65d9d', usage=CompletionUsage(completion_tokens=79, prompt_tokens=989, total_tokens=1068, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0, text_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=None, cached_tokens=0, image_tokens=None, text_tokens=None)))

print(f"Response: {response.choices[0].message.content}")