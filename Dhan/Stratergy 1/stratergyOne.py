# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:28:09 2024

@author: Administrator
"""
from dhanhq import dhanhq
from dhanhq import marketfeed 
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import time 


stockLists = ['RELIANCE', 'TCS', 'HDFCBANK', 'BHARTIARTL', 'ICICIBANK', 'INFY', 'SBIN', 'HINDUNILVR', 'ITC', 'LICI', 'LT', 'HCLTECH', 'BAJFINANCE', 'SUNPHARMA', 'TATAMOTORS', 'MARUTI', 'NTPC', 'AXISBANK', 'ONGC', 'KOTAKBANK', 'DMART', 'ADANIENT', 'ULTRACEMCO', 'M_M', 'TITAN', 'ASIANPAINT', 'BAJAJ_AUTO', 'POWERGRID', 'ADANIPORTS', 'HAL', 'COALINDIA', 'BAJAJFINSV', 'ADANIGREEN', 'WIPRO', 'TRENT', 'NESTLEIND', 'ADANIPOWER', 'ZOMATO', 'IOC', 'SIEMENS', 'JSWSTEEL', 'JIOFIN', 'IRFC', 'BEL', 'VBL', 'DLF', 'HINDZINC', 'INDIGO', 'LTIM', 'SBILIFE', 'TATASTEEL', 'GRASIM', 'VEDL', 'PIDILITIND', 'PFC', 'ABB', 'TECHM', 'GODREJCP', 'AMBUJACEM', 'HDFCLIFE', 'RECLTD', 'BPCL', 'HINDALCO', 'BRITANNIA', 'DIVISLAB', 'GAIL', 'TATAPOWER', 'CIPLA', 'TVSMOTOR', 'EICHERMOT', 'JSWENERGY', 'CHOLAFIN', 'MOTHERSON', 'SHRIRAMFIN', 'HAVELLS', 'BANKBARODA', 'ADANIENSOL', 'TATACONSUM', 'LODHA', 'PNB', 'DABUR', 'TORNTPHARM', 'RVNL', 'INDUSTOWER', 'BAJAJHLDNG', 'HEROMOTOCO', 'ZYDUSLIFE', 'SUZLON', 'UNITDSPR', 'INDUSINDBK', 'DRREDDY', 'IOB', 'ICICIPRULI', 'CGPOWER', 'ICICIGI', 'CUMMINSIND', 'POLYCAB', 'LUPIN', 'COLPAL', 'APOLLOHOSP']

def get_stock_details(stock):
    Company = TA_Handler(
        symbol= stock,
        screener="india",
        exchange="NSE",
        interval=Interval.INTERVAL_1_DAY
    )
    Indicators = Company.get_analysis().indicators
    analysys = Company.get_analysis()
    #print(Indicators['SMA200'])
    #print(Indicators['close']) 
    #print(analysys.summary)
    print(stock)
    if Indicators['close'] > Indicators['SMA200'] and (analysys.summary['RECOMMENDATION'] == 'BUY' or analysys.summary['RECOMMENDATION'] == 'STRONG_BUY'):
        print(stock)

for stock in stockLists:
    get_stock_details(stock)
    