import openai
from openai import OpenAI
import numpy as np
from Vectors.Vectors_Hidden import YOUR_API_KEY
from langchain_openai import OpenAIEmbeddings
import json

client = OpenAI(api_key=YOUR_API_KEY)
messages = [ {"role": "system", "content": "You are designed to assist Proctor Students."} ]


while True: 
    message = input("User : ") 
    if message: 
        messages.append(
            {"role": "user", "content": message},
        ) 
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
      
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})