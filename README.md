# **Project-zoomcamp: Bitcoin Data**
This is a simple Bitcoin data pipeline which extracts the data from the Nasdaq Data Link API and uploads it to Google BigQuery using Python scripts. It is then displayed using Google Looker Studio.

Besides the initial extraction of all the data, I've deployed another Python script in GCP using Pub/Sub, Google Cloud Functions and Google Cloud Scheduler to automatically update the table every day with data for the previous day.

## Tools I'm using
- WSL running Ubuntu 22.04
- Conda 22.9.0 with Python 3.10.6
- Nasdaq Data Link API
- GCP: BigQuery, Pub/Sub, Cloud Functions, Cloud Scheduler, Looker Studio

## Setup
1. In a Command Prompt window, I installed WSL by running: 
    ```
    wsl --install -d Ubuntu-22.04
    ```

2. In the WSL terminal, I set up Anaconda by following the next steps:
    - I downloaded Anaconda by running:
        ```
        wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
        ```
        Then to install and set it up:
        ```
        bash ~/PATH_TO_DOWNLOADED_FILE/Anaconda3-2022.10-Linux-x86_64.sh
        ```
    - I followed the prompts to initialise the base Conda environment. Full steps and further information can be found at: https://docs.anaconda.com/free/anaconda/install/linux/#id2

3. I installed the required Python packages:
    ```
    pip3 install -r requirements.txt
    ```

4. I created a Nasdaq Data Link account on https://data.nasdaq.com/sign-up and obtained my free API key.

5. On the home directory in WSL, I ran `nano .bashrc` to open the .bashrc file and then I pasted the following:
    ```
    export NASDAQ_DATA_LINK_APY_KEY='MY_API_KEY'
    ```
    This sets the environment variable that will hold the API key.

6. I've created a new project in GCP and set up the necessary IAM permissions, along with enabling and setting up each tool mentioned before as needed. The region settings I've selected are based on their free tier as detailed here: https://cloud.google.com/free/docs/free-cloud-features

## Initial extraction run
1. While on the main project directory, I run: 
    ```
    python3 initial_upload.py
    ```
    This will extract all the data from the API up to the previous day, and upload it to a BigQuery table.

## Automated extraction run
For this, I'm using Google's Cloud Scheduler, Pub/Sub and Cloud Functions.

1. On the Pub/Sub screen, I created a new topic called "cloud-function-trigger"
    
    ![Pub/Sub](/images/PubSub_topic.jpg)

2. On the Cloud Functions screen:

    - I created a new function called "btc-daily-update" using the Pub/Sub topic I created as the trigger. I also added the environment variable with the API key.
    
        ![Cloud function creation](/images/Cloud_function_1.jpg)

    - Then, I uploaded a zip file containing main.py, daily_extraction.py and requirements.txt to a GCP bucket.
    
        ![Cloud function code upload](/images/Cloud_function_2.jpg)

    - Lastly, I deployed the code to create the cloud function.
    
        ![Cloud function deployment](/images/Cloud_function_3.jpg)

3. I created a job in Cloud Scheduler to send a message to the Pub/Sub topic on a cron schedule.

    ![Cloud Scheduler](/images/Cloud_Scheduler.jpg)

Cloud Scheduler publishes a Pub/Sub message on a desired schedule. This message gets published to the Pub/Sub topic. This topic then triggers the cloud function and executes the script that I deployed.