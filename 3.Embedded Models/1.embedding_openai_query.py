from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

res = embedding.embed_query("Delhi is the capital of india") # for single query

res = embedding.embed_documents([
    "Delhi is the capital of india",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
])  # for multiple queries.

print(res)