import nasdaqdatalink
import pandas as pd
import functools as ft

from datetime import date, timedelta

# To get yesterday's date
start_date = date.today() - timedelta(days=1)

# Transforms the date to a string to be used by the API
start_date = start_date.strftime("%Y-%m-%d")

# From here on, it's the same as extraction.py
bitcoin = nasdaqdatalink.get('BCHAIN/MKPRU', start_date=start_date)
bitcoin.columns=["Price_USD"]
print("MKPRU: Price_USD has been added to the Dataframe.")

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

for code, name in merging_columns.items():
    new_column = nasdaqdatalink.get(f'BCHAIN/{code}', start_date=start_date)
    new_column.columns=[f"{name}"]
    bitcoin = bitcoin.merge(new_column, on="Date")
    print(f"{code}: {name} has been added to the Dataframe.")
