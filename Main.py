import openai
import requests
from ics import Calendar

#This defines the function to download the the webcal to an ics file
def download_ics(webcal_link, ics_filename):
   response = requests.get(webcal_link)
   with open(ics_filename, 'wb') as file:
       file.write(response.content)

#This defines the funtion to convert the ics to txt
def convert_ics_to_txt(ics_filename, txt_filename):
   with open(ics_filename, 'r') as file:
       calendar = Calendar(file.read())
   with open(txt_filename, 'w') as file:
       file.write(str(calendar))

#Combines said functions 
def webcal_to_txt(webcal_link, ics_filename, txt_filename):
   download_ics(webcal_link, ics_filename)
   convert_ics_to_txt(ics_filename, txt_filename)

#Call function
webcal_to_text()

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to read content from a text file
def read_file(file_path):
   with open(file_path, "r") as file:
       return file.read()

# Specify the path to the text file
text_file_path = "your_text_file.txt"

# Read the content of the text file
conversation_history = read_file(text_file_path)

# Create a chat completion using the OpenAI GPT-3.5-turbo model
response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo", # Use the appropriate model
   messages=[
       {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
       {"role": "user", "content": conversation_history},
   ]
)

# Print the generated completion
print(response['choices'][0]['message']['content'])
