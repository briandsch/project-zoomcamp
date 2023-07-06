import pandas as pd
import pandas_gbq

from initial_extraction import bitcoin

# Sets the DataFrame index as a regular column
bitcoin = bitcoin.reset_index()

# Sets the data type of the Date to date only, so that the time doesn't show in BigQuery
schema = [{"name": "Date", "type": "DATE"}]

# Automatically converts data types based on the data in the DataFrame
bitcoin = bitcoin.convert_dtypes()

# Uploads the DataFrame to a new BigQuery table
pandas_gbq.to_gbq(bitcoin, "bitcoin_data.bitcoin_table", "project-zoomcamp", if_exists="replace", table_schema=schema)
