-- Merges the previous View with the filled values into the existing table.

MERGE `project-zoomcamp.bitcoin_data.bitcoin_table` AS bitcoin_table
USING `project-zoomcamp.bitcoin_data.filled_values` AS filled_values
ON bitcoin_table.Date = filled_values.Date

WHEN MATCHED THEN UPDATE SET
    bitcoin_table.Confirmation_Time_Minutes = filled_values.Confirmation_Time_Minutes
