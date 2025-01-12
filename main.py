from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import scrapers.advanced
import scrapers.autozone
import scrapers.napa
import scrapers.oreilly

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

def getProductInput():
    productName = input('What is the product name?\n')
    productNameList=productName.split(' ')
    return productNameList
    
def main():
    
    productName = getProductInput()
    
    print(scrapers.advanced.scrape(productName))
    #scrapers.autozone.scrape(productName)
    print(scrapers.napa.scrape(productName))
    print(scrapers.oreilly.scrape(productName))
    
    

if __name__ == "__main__":
    main()