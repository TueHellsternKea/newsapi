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

# API
You have to registry for a API key to get this to work.

It is free and you do it at: [newscatcherapi.com](https://newscatcherapi.com/)

When you have confirmed your email, you get access to your API key

![](./image/news_api.jpg)

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
