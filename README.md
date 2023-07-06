# **Project-zoomcamp: Bitcoin Data**
This is a simple Bitcoin data pipeline which extracts the data from the Nasdaq Data Link API and uploads it to Google BigQuery using Python scripts. It is then displayed using Google Looker Studio.

Besides the initial extraction of all the data, I've deployed another Python script in GCP using Pub/Sub, Google Cloud Functions and Google Cloud Scheduler to automatically update the table every day with data for the previous day.

I've called this "Project-zoomcamp" as this is my first data pipeline after completing the [Data Engineering Zoomcamp by DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp). I take the opportunity to give thanks to them for putting together such a well explained and comprehensive course; I definitely learned a lot from it, despite me deciding to start off with a rather simple data pipeline compared to what they covered in the course.

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

5. On the home directory in WSL, I ran `nano .bashrc` to open the .bashrc file and then I added the following line:
    ```
    export NASDAQ_DATA_LINK_APY_KEY='MY_API_KEY'
    ```
    Needless to say, "MY_API_KEY" needs to be replaced with the actual key. This sets the environment variable that will hold the API key.

6. I've created a new project in GCP and set up the necessary IAM permissions, along with enabling and setting up each tool mentioned before as needed. The region settings I've selected are based on their free tier as detailed here: https://cloud.google.com/free/docs/free-cloud-features

## Initial extraction run
1. With the terminal on the main project directory, I run: 
    ```
    python3 initial_upload_gcp.py
    ```
    This will extract all the data from the API up to the previous day, and upload it to a BigQuery table.

## Automated extraction run
For this, I'm using Google's Cloud Scheduler, Pub/Sub and Cloud Functions.

1. On the Pub/Sub screen, I created a new topic called "cloud-function-trigger"
    
    ![Pub/Sub](/images/PubSub_topic.jpg)

2. On the Cloud Functions screen:

    - I created a new function called "btc-daily-update" using the Pub/Sub topic I created as the trigger. I also added the environment variable with the API key.
    
        ![Cloud function creation](/images/Cloud_Function_1.jpg)

    - I uploaded a zip file containing `main.py`, `daily_extraction.py` and `requirements.txt` to a GCP bucket to then select it for my function.
    
        ![Cloud function code upload](/images/Cloud_Function_2.jpg)

    - Lastly, I deployed the code to create the cloud function.
    
        ![Cloud function deployment](/images/Cloud_Function_3.jpg)

3. I created a job in Cloud Scheduler to send a message to the Pub/Sub topic on a cron schedule.

    ![Cloud Scheduler](/images/Cloud_Scheduler.jpg)

Cloud Scheduler publishes a Pub/Sub message on a desired schedule. This message gets published to the Pub/Sub topic. This topic then triggers the cloud function and executes the script that I deployed.

## SQL Scripts
There is a period of time in the column `Confirmation_Time_Minutes` where there are null values on two out of every three days. Given how consistent this pattern is, along with the fact that the values are null, I assume that there was an issue during this period when this data was being either generated or collected. 

To approximate, and to avoid the graph looking bad, I've decided to use the `last_value()` function to smooth things out by filling in the blanks with the last existing value. I've first created a view using this function, and then on a separate script, I've merged this view with the main table.

## Google Looker Studio
I have created a [Google Looker Studio report](https://lookerstudio.google.com/reporting/15ac012e-02e0-4c87-a454-44e75ace4b87/page/A46UD) to display all the data. Given that for this project I'm only using Bitcoin data, there are many charts and controls that I can't meaningfully use.

On page 1, I made a very simple dashboard to show recent price data.

On page 2, I created a chart for each different metric with a date control at the top to easily compare how each metric progressed over the same selected period of time.