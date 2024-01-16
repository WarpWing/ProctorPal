import openai
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import numpy as np
from Hidden import YOUR_API_KEY
from langchain_openai import OpenAIEmbeddings



embeddings_model = OpenAIEmbeddings(openai_api_key=YOUR_API_KEY)


n = 0

openai.api_key = YOUR_API_KEY
with open('Vectors/handbook_output.txt', 'r') as f:
    text = f.read()
    text2 = text.split(".")

while(n != len(text2)):

    embedded_query = embeddings_model.embed_query(text2[n])
    embedded_query[:5]

n += 1