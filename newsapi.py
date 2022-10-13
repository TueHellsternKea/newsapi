# Import packages
import time
import csv
import os
import json

# Preinstalled packages
import requests
import pandas as pd
import configparser

# Folder to save your .csv files
# Windows
#os.chdir('C:\\Users\\tuehe\\Documents\\GitHub\\newsapi')

# macOS
#os.chdir('/Users/user_name/newsapi')

# URL of our News API
base_url = 'https://api.newscatcherapi.com/v2/search'

# Your API key from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
X_API_KEY = config.get('newsreader', 'api_key')

# Make an API call
headers = {'x-api-key': X_API_KEY}

# Define your desired parameters
params = {
    'q': 'Python and Excel',
    'lang': 'en',
    'to_rank': 10000,
    'page_size': 100,
    'page': 1
    }

# Make a call with both headers and params
response = requests.get(base_url, headers=headers, params=params)

# Encode received results
results = json.loads(response.text.encode())
if response.status_code == 200:
    print('Done')
else:
    print(results)
    print('ERROR: API call failed.')

# Import data into pandas
pandas_table = pd.DataFrame(results['articles'])

#print(pandas_table)

# Generate CSV from Pandas table
pandas_table.to_csv('extracted_news_articles.csv', encoding='utf-8', sep=';')
