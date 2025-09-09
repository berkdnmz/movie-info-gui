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

    movie['added_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    movies.append(movie)

    with open(filepath, 'w') as f:
        json.dump(movies, f, indent=4)

def load_movie_list(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def get_window_geometry(root, width_ratio=0.7, height_ratio=0.85):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = int(screen_width * width_ratio)
    height = int(screen_height * height_ratio)

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) - 40

    return f"{width}x{height}+{x}+{y}"

def clean_value(value: str) -> str:
    return '-' if not value or value == 'N/A' else value