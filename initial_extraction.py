import nasdaqdatalink
import pandas as pd
import functools as ft
from datetime import date, timedelta

end_date = date.today() - timedelta(days=1)

start_date = ''
# end_date = ''

# Gathers the data into a DataFrame for the dates specified above
bitcoin = nasdaqdatalink.get('BCHAIN/MKPRU', start_date=start_date, end_date=end_date)
bitcoin.columns=["Price_USD"]
print("MKPRU: Price_USD has been added to the Dataframe.")

# Dictionary with column identifiers and names, to use for merging
merging_columns = {
"ETRAV": "Transaction_Volume",
"ETRVU": "Transaction_Volume_USD",
"HRATE": "Hash_Rate",
"DIFF": "Difficulty",
"MKTCP": "Market_Cap",
"NTRAN": "Transaction_Count",
"NTRAT": "Transaction_Count_Accumulated",
"TOTBC": "Total_Mined",
"TOUTV": "Output_Volume",
"TRFEE": "TRFees_BTC",
"TRFUS": "TRFees_USD",
"CPTRA": "Cost_Per_Transaction",
"CPTRV": "Cost_Percentage_of_TRVolume",
"AVBLS": "Block_Size_Average",
"NTRBL": "Transactions_Per_Block",
"ATRCT": "Confirmation_Time_Minutes",
"NADDU": "Unique_Addresses_Used",
"MIREV": "Miners_Revenue"
}

# For-loop to gather and merge all the columns into one DataFrame
for code, name in merging_columns.items():
    new_column = nasdaqdatalink.get(f'BCHAIN/{code}', start_date=start_date, end_date=end_date)
    new_column.columns=[f"{name}"]
    bitcoin = bitcoin.merge(new_column, on="Date", how="outer")
    print(f"{code}: {name} has been added to the Dataframe.")
