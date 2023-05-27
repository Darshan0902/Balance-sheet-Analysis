import requests
import matplotlib.pyplot as plt
import seaborn as sns

api_key ="dedwiejkdpdweod" #Get yours at https://site.financialmodelingprep.com/developer/docs/
company = "GOOG"  # make sure you use the ticker symbol.

years = 5  #define the years
balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?periods=quarterly&limit={years}&apikey={api_key}')


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

# Calculating the Debt the company is in :
total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference =  cash_and_equivalents - total_debt
print(f"cash debt difference : {cash_debt_difference:,}")

#calculating the debt of any company ;
total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference = cash_and_equivalents - total_debt
print(f"cash_debt_difference for {company} : {cash_debt_difference :,}")


# calculating the percentage for intangible assets :

goodwill_and_intangibles = balance_sheet[0]['goodwillAndIntangibleAssets']
total_assets = balance_sheet[0]['totalAssets']
percentage_intangible = goodwill_and_intangibles / total_assets
print(f"Percentage intanglible : {percentage_intangible*100}%")


# Defining the Quarters :

assets_q1 = balance_sheet[4]['totalAssets']
assets_q2 = balance_sheet[3]['totalAssets']
assets_q3 = balance_sheet[2]['totalAssets']
assets_q4 = balance_sheet[1]['totalAssets']

# making a  list of this assets :
assets_data = [assets_q1 , assets_q2 , assets_q3 , assets_q4]

#Scaling the values:
assets_data = [x / 1000000000 for x in assets_data]



#Plotting the data :

plt.bar([1,2,3,4] , assets_data)
plt.title("Quarterly assets data of the : {company}")
plt.xlabel("Quarters")
plt.ylabel("Total assets in BILLIONS (USA DOLLARS : [$])")
plt.xticks([1,2,3,4] , ['Q1','Q2','Q3','Q4'])
plt.show()

