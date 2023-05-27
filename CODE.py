
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


#Calculating the Total Assets:
total_current_assets = balance_sheet[0]['totalCurrentAssets']
# Ensure that you have given proper index here in this case '0' specifies the value of the current most entry.
print(f"Total current assets of  {company} : {total_current_assets:,}")


#Calculating the Total Liablilites:
total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
# Ensure that you have given proper index here in this case '0' specifies the value of the current most entry.
print(f"Total current Liabilities of  {company} : {total_current_liabilities:,}")

#calculating the debt of any company ;
total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference = cash_and_equivalents - total_debt
print(f"cash_debt_difference for {company} : {cash_debt_difference :,}")


