# %%
import nasdaqdatalink
import pandas as pd
import functools as ft

# %%
start_date = '2022-05-01'

# %%
price_usd = nasdaqdatalink.get('BCHAIN/MKPRU', start_date=start_date)
transaction_vol = nasdaqdatalink.get('BCHAIN/ETRAV', start_date=start_date)
transaction_vol_usd = nasdaqdatalink.get('BCHAIN/ETRVU', start_date=start_date)
hashrate = nasdaqdatalink.get('BCHAIN/HRATE', start_date=start_date)
difficulty = nasdaqdatalink.get('BCHAIN/DIFF', start_date=start_date)
market_cap = nasdaqdatalink.get('BCHAIN/MKTCP', start_date=start_date)
transactions_count = nasdaqdatalink.get('BCHAIN/NTRAN', start_date=start_date)
transactions_count_accum = nasdaqdatalink.get('BCHAIN/NTRAT', start_date=start_date)
total_mined = nasdaqdatalink.get('BCHAIN/TOTBC', start_date=start_date)
output_volume = nasdaqdatalink.get('BCHAIN/TOUTV', start_date=start_date)
trfees_btc = nasdaqdatalink.get('BCHAIN/TRFEE', start_date=start_date)
trfees_usd = nasdaqdatalink.get('BCHAIN/TRFUS', start_date=start_date)
cost_per_transaction = nasdaqdatalink.get('BCHAIN/CPTRA', start_date=start_date)
cost_percentage_of_trvolume = nasdaqdatalink.get('BCHAIN/CPTRV', start_date=start_date)
block_size_avg = nasdaqdatalink.get('BCHAIN/AVBLS', start_date=start_date)
transactions_per_block = nasdaqdatalink.get('BCHAIN/NTRBL', start_date=start_date)
confirmation_time_minutes = nasdaqdatalink.get('BCHAIN/ATRCT', start_date=start_date)
unique_addresses_used = nasdaqdatalink.get('BCHAIN/NADDU', start_date=start_date)
miners_revenue = nasdaqdatalink.get('BCHAIN/MIREV', start_date=start_date)

# %%
price_usd.columns=["Price_USD"]
transaction_vol.columns=["Transaction_Volume"]
transaction_vol_usd.columns=["Transaction_Volume_USD"]
hashrate.columns=["Hash_Rate"]
difficulty.columns=["Difficulty"]
market_cap.columns=["Market_Cap"]
transactions_count.columns=["Transaction_Count"]
transactions_count_accum.columns=["Transaction_Count_Accumulated"]
total_mined.columns=["Total_Mined"]
output_volume.columns=["Output_Volume"]
trfees_btc.columns=["TRFees_BTC"]
trfees_usd.columns=["TRFees_USD"]
cost_per_transaction.columns=["Cost_Per_Transaction"]
cost_percentage_of_trvolume.columns=["Cost_Percentage_of_TRVolume"]
block_size_avg.columns=["Block_Size_Average"]
transactions_per_block.columns=["Transactions_Per_Block"]
confirmation_time_minutes.columns=["Confirmation_Time_Minutes"]
unique_addresses_used.columns=["Unique_Addresses_Used"]
miners_revenue.columns=["Miners_Revenue"]

# %%
data_frames = [
    price_usd,
    transaction_vol,
    transaction_vol_usd,
    hashrate,
    difficulty,
    market_cap,
    transactions_count,
    transactions_count_accum,
    total_mined,
    output_volume,
    trfees_btc,
    trfees_usd,
    cost_per_transaction,
    cost_percentage_of_trvolume,
    block_size_avg,
    transactions_per_block,
    confirmation_time_minutes,
    unique_addresses_used,
    miners_revenue
    ]

# %%
bitcoin = ft.reduce(lambda left,right: pd.merge(left,right,on=['Date'], how='inner'), data_frames)



