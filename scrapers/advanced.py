from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def createSearchURLAdvanced(productNameList):
    searchURL = 'https://shop.advanceautoparts.com/web/SearchResults?searchTerm='
    #'5w30+motor+oil&autoSuggest=false&recentSearch=false&storeId=10151&catalogId=10051&langId=-1'
    
    for i in range(len(productNameList)):
        searchURL += productNameList[i]
        
        if (i < len(productNameList)-1):
            searchURL += '+'
        
    return searchURL
    
def scrape(productName):
    name = createSearchURLAdvanced(productName)
    return name