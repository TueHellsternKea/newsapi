# Newscatcher
Demo of the Newscatcher API

    Search multi-language worldwide news articles published online with NewsCatcher's News API

In this demo I'm getting news articles regarding **Python and Excel**

![](./image/news_1.jpg)

# Files
- *newsapi.py*
- *requirements.txt*
- *config.ini*
- *extracted_news_articles.csv*
- *.gitignore*

![](./image/news_2.jpg)

# API - Newscatcher
You have to registry for a API key to get this to work.

It is free and you do it at: [newscatcherapi.com](https://newscatcherapi.com/)

When you have confirmed your email, you get access to your API key

![](./image/news_api.jpg)

## newsapi.py
The Python code file

```python
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
```


## config.ini
You have to put *your* API key in the **config.ini** file:

```txt
[newsreader]
api_key = o1xxxxxxxxxxxxxxxxxxxxxxxxxxxx7wY
```
The **config.ini** file is include in **.gitignore**

# How to run
- Clone this GitHub Repository to your local computer
- Make a new Virtual Environment in the GitHub folder - **news_env**
- **cd** into **news_env**
- Activate the Virtual Environment
    - **.\Scripts\activate** (*Windows*)
    - ** sourse bin/activate** (*macOS*) 
- **cd** to the folder with the **requirements.txt** file
- Install the necessary modules from the **requirements.txt** file
    - **pip3 install -r requirements.txt**
- Run **newsapi.py**

**Note**: *Make sure that the* **.gitignore** *file include your Virtual Environment* - **news_env** and **config.ini**

# Links
- [newscatcherapi.com](https://newscatcherapi.com/)
- [github.com/NewscatcherAPI/newscatcherapi-sdk-python](https://github.com/NewscatcherAPI/newscatcherapi-sdk-python)
- [github.com/TueHellsternKea/newsapi](https://github.com/TueHellsternKea/newsapi/blob/main/README.md)
