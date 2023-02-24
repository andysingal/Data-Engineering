import requests
import streamlit as st
from send_email import send_email

api_key = "DVav0fgCL3wl71jEf2p1QctzcdIEBIFCxyytdRgq"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

response = requests.get(url)
print(response.status_code)
data = response.json()

#Extract the image title,url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

#Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath,'wb') as file:
      file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)






