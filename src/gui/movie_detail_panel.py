import customtkinter as ctk
from PIL import Image
import requests
from io import BytesIO

class MovieDetailPanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.poster_label = ctk.CTkLabel(self, text='Poster',font=("Impala", 20, "roman"))
        self.poster_label.grid(row=0, column=0, padx=10, pady=10)

        self.info_label = ctk.CTkLabel(self, text='Movie Info', font=("Impala", 20, "roman"),justify='left')
        self.info_label.grid(row=0, column=1, padx=10, pady=10)

    def update_movie(self, movie_data):
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