import json
import os
from datetime import datetime

DATA_DIR = 'data'

def save_movie_list(filename, movie):
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)

    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            movies =json.load(f)
    else:
        movies = []

    movie['added_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    movies.append(movie)

    with open(filepath, 'w') as f:
        json.dump(movies, f, indent=4)

def load_movie_list(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return []