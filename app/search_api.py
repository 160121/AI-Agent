import requests
from config.config import Config

def search(query):
    url = f"https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": Config.SERP_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Search API failed with status code {response.status_code}")
