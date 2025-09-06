import customtkinter as ctk
from PIL import Image
import requests
from io import BytesIO

class MovieDetailPanel(ctk.CTkFrame):
    def __init__(self, master, add_callback = None, watch_callback = None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_movie = None
        self.add_callback = add_callback
        self.watch_callback = watch_callback

        self.poster_label = ctk.CTkLabel(self, text='Poster',font=("Impala", 20, "roman"))
        self.poster_label.grid(row=0, column=0, padx=10, pady=10)

        self.info_label = ctk.CTkLabel(self, text='Movie Info', font=("Impala", 20, "roman"),justify='left')
        self.info_label.grid(row=0, column=1, padx=10, pady=10)

        self.add_fav_button = ctk.CTkButton(self, text='Add to Favorites', command=self.add_to_favorites)
        self.add_fav_button.grid(row=2, column=0, pady=5)

        self.add_watch_button = ctk.CTkButton(self, text='Add to Watch', command=self.add_to_watch)
        self.add_watch_button.grid(row=2, column=2, pady=5)

    def update_movie(self, movie_data):
        self.current_movie = movie_data
        poster_url = movie_data.get('Poster')
        if poster_url and poster_url !='N/A':
            response = requests.get(poster_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((200, 300))
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(200, 300))
            self.poster_label.configure(image=ctk_image, text='')
            self.poster_label.image = ctk_image
        else:
            self.poster_label.configure(text='No Poster', image='')

        info_text = (
            f"Title: {movie_data.get('Title', '-')}\n"
            f"Year: {movie_data.get('Year', '-')}\n"
            f"Genre: {movie_data.get('Genre', '-')}\n"
            f"IMDb: {movie_data.get('imdbRating', '-')}\n"
            f"Director: {movie_data.get('Director', '-')}\n"
            f"Actors: {movie_data.get('Actors', '-')}"
        )
        self.info_label.configure(text=info_text)

    def add_to_favorites(self):
        if self.current_movie and self.add_callback:
            self.add_callback(self.current_movie)

    def add_to_watch(self):
        if self.current_movie and self.watch_callback:
            self.watch_callback(self.current_movie)