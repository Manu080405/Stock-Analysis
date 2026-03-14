import yfinance as yf

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)

    result = data.reset_index().to_dict(orient="records")
    return result