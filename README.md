# Google Play Store Scraper using Selenium and Python
# Description
This repository contains a Python script that utilizes Selenium to scrape data from the Google Play Store. The script enables users to retrieve information about their desired apps, such as app name, developer name, ratings, reviews, and other relevant details. The scraped data is then saved in a CSV file for easy analysis and further processing.

# Features
Scrapes data from the Google Play Store for a specified app.
Retrieves app details such as name, developer, category, ratings, reviews, and more.
Saves the scraped data into a CSV file for convenient data handling.
Supports customizable parameters for scraping specific information.
# Installation
To use this script, you will need to follow these steps:

# Clone the repository:



git clone https://github.com/theawaisahmadkhan/Google-Play-Store-Scrapper-Selenium-Python.git
cd Google-Play-Store-Scrapper-Selenium-Python
Install the required dependencies using pip:



pip install -r requirements.txt
Download and install the appropriate web driver for your browser. The script currently supports Chrome browser (chromedriver) and Firefox browser (geckodriver). Ensure that the web driver is added to your system's PATH.

# Usage
Open the google_play_scraper.py script.

Modify the app_url variable with the URL of the Google Play Store app you want to scrape. For example:

python
app_url = "https://play.google.com/store/apps/details?id=com.example.app"
Run the script:

python Google Play store Scrap.py
After execution, the script will fetch the desired app's information and save it in a CSV file named app_data.csv.
