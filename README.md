

# Real-Time Stock Market Dashboard

## 📌 Project Overview
The **Real-Time Stock Market Dashboard** is a Python-based web application built using **Streamlit** that allows users to monitor and visualize live stock market data.  
This dashboard provides a simple and interactive interface for tracking stock prices, analyzing trends, and making informed decisions.  

It is designed to be beginner-friendly and can be used for educational purposes, portfolio tracking, or data analysis practice.

---

## 🚀 Features
- **Live Stock Data Visualization:** Fetches real-time stock data using Yahoo Finance (`yfinance` library).  
- **Customizable Date Range:** Users can select any start and end date to view historical stock data.  
- **Interactive Line Chart:** Displays the stock’s closing prices over the selected period.  
- **Data Table:** Shows complete stock information including Open, High, Low, Close, Adj Close, and Volume.  
- **Dynamic Ticker Input:** Users can search any company stock by entering its ticker symbol (e.g., `AAPL`, `GOOGL`).  
- **User-Friendly Interface:** Streamlit provides an intuitive UI that runs in the browser.  

---

## 🛠️ Technologies Used
| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Streamlit  | Web app interface for interactive dashboards |
| yfinance   | Fetch stock market data from Yahoo Finance |
| pandas     | Data manipulation and analysis |
| matplotlib / Streamlit charts | Plotting stock price trends |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Stock_Market_Dashboard

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Dashboard

streamlit run app.py

5. Open in Browser

Once Streamlit starts, it will provide a local URL (usually http://localhost:8501). Open it in your browser to interact with the dashboard.


---

📊 How to Use

1. Enter a stock ticker symbol in the sidebar (e.g., AAPL, MSFT).


2. Select a start date and end date to define the period for stock data visualization.


3. The dashboard will display:

An interactive line chart showing the stock’s closing prices.

A data table showing Open, High, Low, Close, Adj Close, and Volume values.



4. Explore the trends and analyze the stock performance over your selected period.




---

🔍 Example

Ticker: AAPL

Start Date: 2023-01-01

End Date: 2023-12-31


Output:

Line chart showing Apple’s stock closing prices across the year.

Table with daily stock values for reference.



---

📂 Project Structure

Stock_Market_Dashboard/
│── app.py              # Main Streamlit application
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation


---

💡 Future Enhancements

Add technical indicators (Moving Averages, RSI, MACD) for better analysis.

Include comparison between multiple stocks.

Add downloadable CSV export for analyzed data.

Implement alerts/notifications for stock price changes.

Enhance UI with more charts and visuals using Plotly or Matplotlib.



---

📚 References

Streamlit Documentation

yfinance Documentation

Pandas Documentation




