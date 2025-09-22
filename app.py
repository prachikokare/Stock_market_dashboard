import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

st.title("Real-Time Stock Market Dashboard")

# Sidebar inputs
ticker = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.date(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Fetch stock data
data = yf.download(ticker, start=start_date, end=end_date)

st.write(f"### Stock Data for {ticker}")
st.line_chart(data['Close'])

st.write("### Data Table")
st.dataframe(data)
