import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

def Get_Data(ticker_list,mode):

    
    data = yf.download(ticker_list, interval='1mo',period='max')
    print (data.index)
    data = data['Close'].dropna()
    data['Date'] = data.index
    #mask = (data['Date'] > '2014-01-01')
    #data = data.loc[mask]
    if mode == "Annual":
        data = data[data['Date'].dt.month==1]
    elif mode == "Semi-Annual":
        data = data[data['Date'].dt.month.isin([1, 6])]
    elif mode == "Quaterly":
        data = data[data['Date'].dt.month.isin([1,3,6,9])]
    elif mode == "Monthly":
        pass
        

    amount_of_asset = len(ticker_list)
    return data

def Get_Latest_Data(Tickern):
    price = 0
    try:
        obj = yf.Ticker(Tickern)
        row =  obj.history(period="1d")
        price = float(row["Close"])
    except:
        data = yf.download(str(Tickern), period="5d")
        a = data['Close'].iloc[-1].values
        price = float(a[0])


  
    return price


    

def Get_Daily_Data(ticker_list,start,end):

    
    data = yf.download(ticker_list, interval='1d',start=start, end=end)
    print (data.index)
    data = data['Close'].dropna()
    data['Date'] = data.index
    #mask = (data['Date'] > '2014-01-01')
    #data = data.loc[mask]
    

    amount_of_asset = len(ticker_list)
    return data
def Get_Full_Name(Ticker_list):

    Full_ticker_list = []
    for ticker in Ticker_list:
        ticker_object = yf.Ticker(ticker).info
        Fullname= (ticker_object['longName'])
        Full_ticker_list.append(ticker+' - '+Fullname)

    #
    return (Full_ticker_list)