-- The last_value() function is used to replace the null values with the last existing value as it goes through the column.

-- A View is created out of this to then merge with the existing table.
CREATE VIEW `project-zoomcamp.bitcoin_data.filled_values` AS
      SELECT 
            Date,
            last_value(Confirmation_Time_Minutes IGNORE NULLS) OVER (ORDER BY Date) Confirmation_Time_Minutes,
      FROM `project-zoomcamp.bitcoin_data.bitcoin_table`
      
      -- This range can be changed depending on where the null values are, to avoid running this over the whole table.
      WHERE Date BETWEEN '2018-07-01' AND '2020-04-01'
