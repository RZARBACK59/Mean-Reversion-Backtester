# downloads historical stock data from Yahoo Finance

import yfinance as yf
import pandas as pd

def get_data(ticker, start="2015-01-01"):
    data = yf.download(ticker, start=start, auto_adjust=True)
    return data