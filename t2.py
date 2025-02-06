import yfinance as yf
import pandas as pd


Ticker_list = ["3070.HK", "0P0001HNBM.HK", "VOO", "TLT"] # example list
def Get_Full_Name(Ticker_list):

    Full_ticker_list = []
    for ticker in Ticker_list:
        ticker_object = yf.Ticker(ticker).info
        Fullname= (ticker_object['longName'])
        Full_ticker_list.append(ticker+' - '+Fullname)

    #
    return (Full_ticker_list)

print (Get_Full_Name(Ticker_list))

data = yf.download('VOO', period="1d")
a = data['Close'].iloc[0].values
print (float(a[0]))
Ticker='0P0001HNBM.HK'
data = yf.download(Ticker, period="5d")

a = data['Close'].iloc[-1].values
price = float(a[len(a)-1])
print (price)