from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def createSearchURLNapa(productNameList):
    searchURL = 'https://www.napaonline.com/en/search?text='
    
    for i in range(len(productNameList)):
        searchURL += productNameList[i]
        
        if (i < len(productNameList)-1):
            searchURL += '%20'
            
        if (i == len(productNameList)-1):
            searchURL += '&referer=v2'
    
    return searchURL
    
def scrape(productName):
    name = createSearchURLNapa(productName)
    return name