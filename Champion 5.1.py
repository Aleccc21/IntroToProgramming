#Dictionary of stocks with their ticker symbols and the current listed prices
stocks_dict = {
    "AAPL": 189.10,
    "AMZN": 136.70,
    "DIS": 82.00,
    "GOOGL": 135.40,
    "LULU": 402.60,
    "META": 299.70,
    "MSFT": 331.60,
    "NFLX": 451.60,
    "NVDA": 485.30,
    "TSLA": 253.40
}

#Prompt user for a stock ticker symbol
symbol = input("Please enter a stock ticker symbol:")

#Get method pulls stock from dictionary
#If symbol is not found, it will display a message it was not found
price = stocks_dict.get(symbol, 'A stock with that symbol was not found.')

#If symbol is found, it will display the price
print (price)