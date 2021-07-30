import requests
from bs4 import BeautifulSoup

def fetch(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
        }
    response = requests.get(url, headers = headers)
    return response

def create_soup_object(url):
    response = fetch(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def get_listing_status(soup):
    parent_content = soup.find(id = "content")
    rented_status = parent_content.find_all("div", class_= "status closed status_sold")
    contract_status = parent_content.find_all("div", class_= "status pending status_pending")

    if rented_status or contract_status:
        return (False)
    else:
        return (True)


