from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "python.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

# print(docs[0])
# split the doc int chunk
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400,

)
chunks = text_splitter.split_documents(documents=docs)


#Vector Embedding

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333/",
    collection_name="learning_rag"
)
print("Indexing documents Done")
