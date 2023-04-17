import requests

def get_news(keyword):
    # Set the API endpoint and parameters
    url = 'https://newsapi.org/v2/top-headlines'
    api_key = '88d6438c118643f799cbdea281ecd08f'  # Replace with your NewsAPI API key

    # Set the query parameters
    params = {
        'q': keyword,
        'language': 'en',  # Set language to English
        'pageSize': 4,  # Set number of results per page to 4
        'apiKey': api_key  # Set NewsAPI API key
    }

    # Send API request
    response = requests.get(url, params=params)

    # Check if API request was successful
    if response.status_code == 200:
        news = response.json()
        titles = []
        summaries = []
        dates = []
        URL=[]
        count=0
        for article in news['articles']:
            titles.append(article['title'])
            summaries.append(article['description'])
            dates.append(article['publishedAt'])
            URL.append(article['url'])
            count+=1
        news_dict={'Titles':titles,'Headlines':summaries,'dates':dates,'counts':count,'Links':URL}
        return news_dict
    else:
        print("Failed to fetch news from NewsAPI. Error code:", response.status_code)
        return None


