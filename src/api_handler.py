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

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get('Response') == 'False':
            print(f"OMDb API error for '{title}': {data.get('Error')}")
            return None

        poster_url = data.get('Poster')
        if not poster_url or poster_url == 'N/A' or not poster_url.startswith('http'):
            data['Poster'] = None

        return data

    except requests.Timeout:
        print(f"Timeout while fetching '{title}' from OMDb API")
        return None
    except requests.RequestException as e:
        print(f"HTTP error while fetching '{title}': {e}")
        return None
    except ValueError as e:
        print(f"JSON decode error for '{title}': {e}")
        return None