import requests
from ics import Calendar
from Hidden import webcal_link


# Convert the webcal:// URL to an http:// URL
http_link = webcal_link.replace('webcal://', 'http://')

try:
   response = requests.get(http_link)
   response.raise_for_status() # This will raise an HTTPError if the response was an HTTP error
except requests.exceptions.HTTPError as err:
   print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
   print(f"Request Error: {err}")
else:
   calendar = Calendar(response.text)

#This defines the function to download the the webcal to an ics file
def download_ics(webcal_link, ics_filename):
 headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
 }
 response = requests.get(webcal_link, headers=headers)
 with open(ics_filename, 'wb') as file:
     file.write(response.content)

#This defines the funtion to convert the Calendar ics file to a txt file
def convert_ics_to_txt(ics_filename, txt_filename):
   with open(ics_filename, 'r') as file:
       calendar = Calendar(file.read())
   with open(txt_filename, 'w') as file:
       file.write(str(calendar))

#Combines above functions 
def webcal_to_txt(webcal_link, ics_filename, txt_filename):
   download_ics(webcal_link, ics_filename)
   convert_ics_to_txt(ics_filename, txt_filename)

#Defines a function to clear an ics file
def clear_calendar_ics_file(ics_filename):
   with open(ics_filename, 'w') as file:
       pass
#Defines a function to clear an txt file
def clear_calendar_txt_file(txt_filename):
  with open(txt_filename, 'w') as file:
      pass
  

#Defines function to set up Background_Informaion
def set_up_Background_Informaion(txt_filename):
   with open('Calandar.txt', 'r') as file:
       calendar_txt = Calendar(file.read())
   with open('Background_Information.txt', 'w') as file:
       file.write(str(calendar_txt))
     
      


#Call functions to clear Calendar ics and txt files inorder to update them with the new information
clear_calendar_ics_file('Calendar.ics')
clear_calendar_txt_file('Calendar.txt')

#Call function to convert the webcal into a ics file, and then into a txt file
webcal_to_txt(http_link, 'Calendar.ics', 'Calendar.txt')
