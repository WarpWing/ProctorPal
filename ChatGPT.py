from Vectors.Hidden import YOUR_API_KEY
from openai import OpenAI

client = OpenAI(api_key=YOUR_API_KEY)

# Primitive Context Injection
def get_context_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Initial System Prompt
messages = [{"role": "system", "content": "You are a objective system assistant named ProctorPal that helps with answering questions related to Proctor Academy. You do it objectively because objectively you're objective."}]
context = get_context_from_file('Proctor_Handbook_2023_2024_092523_1.txt')  

while True:
    user_message = input("User : ")
    if user_message:
        messages.append({"role": "user", "content": user_message})
        combined_message = context + "\n\n" + user_message
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": combined_message}])
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
