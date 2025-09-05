import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY =os.getenv('API_KEY')
BASE_URL = 'http://www.omdbapi.com/'

def fetch_movie_data(title):
    params = {
        't': title,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None