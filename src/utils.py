import json
import os
from datetime import datetime

DATA_DIR = 'data'

def save_movie_list(filename, movie):
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)

    movies = []
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, 'r', encoding='utf-8') as f:
            movies = json.load(f)

    movie['added_at'] = datetime.now().strftime('%Y-%m-%d')
    movies.append(movie)

    with open(filepath, 'w') as f:
        json.dump(movies, f, indent=4)

def load_movie_list(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []