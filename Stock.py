import yfinance as yf

def show_menu():
    print("\nStock Analysis Menu:")
    print("1. View Available Stock Tickers")
    print("2. Input Stock Tickers and Date Range to Check")
    print("3. Exit")

def show_available_stocks():
    available_stocks = ['TSLA - Tesla', 'AMZN - Amazon', 'AMD - AMD', 'GME - GameStop']
    print("\nAvailable Stock Tickers:")
    for stock in available_stocks:
        print(stock)

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    print("\nStock Data Retrieved:")
    print(data.head())

def input_stocks_to_check():
    tickers_input = input("Enter stock tickers : ")
    tickers = tickers_input.split(',')
    tickers = [ticker.strip() for ticker in tickers]  
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    get_stock_data(tickers, start_date, end_date)

def main():
    while True:
        show_menu()
        choice = input("Please select an option : ")

        if choice == '1':
            show_available_stocks() 
        elif choice == '2':
            input_stocks_to_check()
        elif choice == '3':
            print("Exiting program.")
            break 
        else:
            print("Invalid choice.")

main()
