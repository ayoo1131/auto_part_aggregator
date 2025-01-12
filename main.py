import scrapers.autozone

def main():

    productName = input('What is the product name?\n')
    productNameList=productName.split(' ')                                                                                                              

    scrapers.autozone.scrape(productNameList)



if __name__ == "__main__":
    main()

