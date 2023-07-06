import pandas as pd
import pandas_gbq

from daily_extraction import bitcoin

# To set the DataFrame index as a regular column
bitcoin = bitcoin.reset_index()

# To set the data type of the Date to date only, so that the time doesn't show in BigQuery
schema = [{"name": "Date", "type": "DATE"}]

# Automatically converts data types based on the data in the DataFrame
bitcoin = bitcoin.convert_dtypes()

# Appends the DataFrame to the existing BigQuery table
pandas_gbq.to_gbq(bitcoin, "bitcoin_data.bitcoin_table", "project-zoomcamp", if_exists="append", table_schema=schema)
