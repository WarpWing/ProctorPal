import openai
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import numpy as np
from Hidden import YOUR_API_KEY


openai.api_key = YOUR_API_KEY
with open('Cache.txt', 'r') as f:
    cache = f.read()
   
response = openai.Embedding.create(
    input=cache,
    model="text-embedding-ada-002" # Imagine not using davinci but ok bro lol
)

embeddings = response['data'][0]['embedding'] # get the actual embeddings
embeddings_array = np.array(embeddings) # turn them into an actual Numpy Array
qdrant_client = QdrantClient(host='localhost', port=6333) #qdrant client connection
points = [PointStruct(id=i, vector=vec.tolist()) for i, vec in enumerate(embeddings_array)] # change them to vector embeddings

collection_name = 'procciepal' # Vector Collection name
qdrant_client.upsert(
    collection_name=collection_name,
    points=points
)
