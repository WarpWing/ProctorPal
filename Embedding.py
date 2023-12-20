import openai
from Hidden import YOUR_API_KEY

openai.api_key=YOUR_API_KEY
response = openai.Embedding.create(
  input="More than a physical place, Proctor is a set of beneficial relationships.",
  model="text-embedding-ada-002"
)

print(response)
