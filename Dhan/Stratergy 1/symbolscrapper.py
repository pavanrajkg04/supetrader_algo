# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:20:27 2024

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
symbolList = []

#url = "https://in.tradingview.com/markets/stocks-india/market-movers-small-cap/"

url = "https://in.tradingview.com/markets/stocks-india/market-movers-large-cap/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
symbol_table = soup.find_all("a" , class_="apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat")

for symbol in symbol_table:
    symbolList.append(symbol.text)
    
print(symbolList)
