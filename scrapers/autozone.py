from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def createSearchURLAutozone(productNameList):
    searchURL = 'https://www.autozone.com/searchresult?searchText='
    
    for i in range(len(productNameList)):
        searchURL += productNameList[i]
        
        if (i < len(productNameList)-1):
            searchURL += '%20'
    
    return searchURL
    
def scrape(productName):
    
    options = Options()
    options.add_argument('--headless')  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.41 Safari/537.36")
    #options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    
    #**May not work
    proxy = "216.229.112.25:8080" 
    options.add_argument(f'--proxy-server={proxy}')
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    #Create URL to send HTTP request to
    autoZoneSearchURL = createSearchURLAutozone(productName)
    
    #autoZonePage = requests.get(autoZoneSearchURL, headers = headers)
    autoZonePage = driver.get(autoZoneSearchURL)
    
    time.sleep(5)
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    
    #This will scrape the raw HTML file and put it in a txt file
    with open('rawtext.txt', 'w') as file:
        file.write(str(soup))
    
    

    '''
    cards = soup.find_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})
    print(len(cards))
    '''
