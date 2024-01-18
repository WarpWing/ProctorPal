import openai
from qdrant_client import QdrantClient
from Vectors.Vectors_Hidden import YOUR_API_KEY
from langchain_openai import OpenAIEmbeddings
openai.api_key = YOUR_API_KEY
from ChatGPT import query

def vector_query(query):

    embeddings_model = OpenAIEmbeddings(openai_api_key=YOUR_API_KEY)


    embedded_query = embeddings_model.embed_query(query)
    embedded_query[:5]

    client = QdrantClient("localhost", port=6333)

    search_result = client.search(
        collection_name="test_collection4", query_vector=embedded_query, limit=5
    )



