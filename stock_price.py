import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
@sigitbaskoro > 2022.03.14\n
Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data oon this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical data of this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open  High  Low  Close  Volume  Dividends  Stock  Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)