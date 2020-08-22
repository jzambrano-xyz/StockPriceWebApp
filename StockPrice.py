#Define libraries to import and use in the project
import yfinance as yf
import streamlit as st
import pandas as pd

#The function st.write allows us to use Markdown in the Web app
st.write("""
# Simple stock price app

Shown are the stock **closing price** and **volume** for Google (GOOGL)!

""")

#Define the ticker symbol to display
tickerSymbol = 'GOOGL'
#Get the data from this ticker
tickerData = yf.Ticker(tickerSymbol)
#Set the range of historical prices to get for this ticker
tickerHp = tickerData.history(period='1d', start='2010-5-31', end='2020-8-21')
#Available data to display:
#Open   High    Low    Close   Volume  Dividends   Stock    Splits

st.line_chart(tickerHp.Close)
st.line_chart(tickerHp.Volume)
