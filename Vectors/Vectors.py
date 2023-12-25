import openai
from Hidden import YOUR_API_KEY

with open('Cache.txt', 'r') as f:
   cache = f.read()

openai.api_key=YOUR_API_KEY
response = openai.Embedding.create(
  input=cache,
  model="text-embedding-ada-002"
)

with open('startup_vectors.npy', 'a') as f:
   f.write("\n"+response)
