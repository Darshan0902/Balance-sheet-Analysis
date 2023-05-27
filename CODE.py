
import requests
import matplotlib.pyplot as plt


api_key =""  #Generate yours from the site : https://site.financialmodelingprep.com/developer/docs/ will attach this in the README.MD as well.

company = "GOOG"  # make sure you use the ticker symbol.
years = 2 #define the years
balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}')




#merging and uploading values in a variable & Formatting it into a JSON format.

balance_sheet = balance_sheet.json()

# Uncomment the below line to check the values available in balance sheet;
#print(balance_sheet)



