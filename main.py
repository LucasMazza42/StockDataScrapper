import requests
from bs4 import BeautifulSoup
import time, threading
from datetime import datetime
import csv



currentStockPrice = 0
priceList = []
def scrap(URL)->str:
    price = ""
    webPage = URL
    page = requests.get(webPage)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.title
    name = name.string

    #get the current price of the stock
    price = soup.find(class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
    price = price.string
    #get the name of the stock
    name = name.split(',')[0]

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(name + " at time " + dt_string + " ---- " + "$" + price)
    priceList.append(price)
    return(price)



while True:
    # Code executed here
    url = 'https://finance.yahoo.com/quote/TSLA?p=AAPL&.tsrc=fin-srch'
    scrap(url)
    time.sleep(5)    
    


