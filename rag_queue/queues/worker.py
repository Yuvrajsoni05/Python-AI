from dotenv import load_dotenv
from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

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
def process_query(query:str):
    print("Searching Chunks ",query)
    search_result = vector_db.similarity_search(query=query)
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
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ]
    )

    print(f"Response: {response.choices[0].message.content}")
    return response.choices[0].message.content