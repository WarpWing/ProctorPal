import openai
from openai import OpenAI
from Vectors.Vectors_Hidden import YOUR_API_KEY
from openai import chat
from qdrant_client import QdrantClient
from Vectors.Vectors_Hidden import YOUR_API_KEY
from langchain_openai import OpenAIEmbeddings
openai.api_key = YOUR_API_KEY

query = input("User: ")

client = OpenAI(api_key=YOUR_API_KEY)

embeddings_model = OpenAIEmbeddings(openai_api_key=YOUR_API_KEY)


embedded_query = embeddings_model.embed_query(query)
embedded_query[:5]

client = QdrantClient("localhost", port=6333)

search_result = client.search(
    collection_name="test_collection4", query_vector=embedded_query, limit=5
)

database_response = search_result


messages = [ {"role": "system", "content": "You are designed to assist Proctor Students."} ]



while True: 
    message = (query, database_response)
    if message: 
        messages.append( 
            {"role": "user", "content": message},
        ) 
        chat = chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
      
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})