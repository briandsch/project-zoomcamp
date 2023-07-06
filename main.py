import base64
import pandas as pd
import pandas_gbq

def update_to_gcp():
    from daily_extraction import bitcoin

    # See "daily_upload_gcp.py"
    bitcoin = bitcoin.reset_index()

    schema = [{"name": "Date", "type": "DATE"}]

    bitcoin = bitcoin.convert_dtypes()

    pandas_gbq.to_gbq(bitcoin, "bitcoin_data.bitcoin_table", "project-zoomcamp", if_exists="append", table_schema=schema)

# Default function from Google's Cloud Functions tool
def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    update_to_gcp()

if __name__ == "__main__":
    hello_pubsub("data", "context")
