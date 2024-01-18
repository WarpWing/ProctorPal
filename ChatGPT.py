import openai
from openai import OpenAI
from Vectors.Vectors_Hidden import YOUR_API_KEY
from qdrant_client import QdrantClient
from Vectors.Vectors_Hidden import YOUR_API_KEY
from langchain_openai import OpenAIEmbeddings
openai.api_key = YOUR_API_KEY


oclient = OpenAI(api_key=YOUR_API_KEY)
embeddings_model = OpenAIEmbeddings(openai_api_key=YOUR_API_KEY)
qclient = QdrantClient("localhost", port=6333)

stop = "no"

while 1 == 1:

    query = input("User: ")
    
    if query == "stop":
        break

    embedded_query = embeddings_model.embed_query(query)
    embedded_query[:5]


    database_response = qclient.search(
        collection_name="test_collection4", query_vector=embedded_query, limit=5
    )

    messages = [ {"role": "system", "content": "You are designed to assist Proctor Students."} ]

    #print(str(database_response))

 
    message = (str(query), str(database_response))
    if message: 
        messages.append( 
            {"role": "user", "content": str(database_response)},
        ) 
        chat = oclient.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
      
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})