import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def listing_status(listing_url):
    opts = Options()
    opts.add_argument(" --headless")
    opts.binary_location= os.getcwd() +'\\GoogleChromePortable\GoogleChromePortable.exe'
    chrome_driver = os.getcwd() +"\\chromedriver.exe"
    driver = webdriver.Chrome()
    driver.get(listing_url)

    soup_file=driver.page_source
    soup = BeautifulSoup(soup_file, "html.parser")

    parent_content = soup.find(id = "content")

    rented_status = parent_content.find_all("div", class_= "status closed status_sold")
    contract_status = parent_content.find_all("div", class_= "status pending status_pending")

    if rented_status:
        return ('Rented')
    elif contract_status:
        return ('In contract')
    else:
        return ('Currently available')


print(listing_status("https://streeteasy.com/building/126-elizabeth-street-new_york/9"))
