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
