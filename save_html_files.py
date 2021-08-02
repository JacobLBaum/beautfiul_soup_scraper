import requests
from scraper import fetch

url = "https://streeteasy.com/building/444-east-78-street-new_york/2?featured=1"
response = fetch(url)
content = response.content
r = requests.get(url)
with open('available_listing3.txt', 'w', encoding="utf-8") as file:
    file.write(content.decode("utf-8"))