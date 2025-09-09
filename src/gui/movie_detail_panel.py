import customtkinter as ctk
from PIL import Image
import requests
from io import BytesIO
import webbrowser

class MovieDetailPanel(ctk.CTkFrame):
    def __init__(self, master, add_callback = None, watch_callback = None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_movie = None
        self.add_callback = add_callback
        self.watch_callback = watch_callback
        self.imdb_url = None

        # Poster frame
        self.poster_frame = ctk.CTkFrame(self, corner_radius=10)
        self.poster_frame.grid(row=0, column=0, padx=20, pady=20, sticky='n')

        self.poster_label = ctk.CTkLabel(self.poster_frame, text='Poster',font=("times", 20, "bold"))
        self.poster_label.grid(row=0, column=0, padx=15, pady=15)


        # Info frame
        self.info_frame = ctk.CTkFrame(self, corner_radius=10)
        self.info_frame.grid(row=0, column=1, padx=20, pady=20, sticky='n')

        # Info movie
        self.title_label = ctk.CTkLabel(self.info_frame, text='Title: -', font=('Times', 25, 'bold'), text_color='white')
        self.title_label.pack(pady=15, padx=15, anchor='w')

        self.year_type_genre_label = ctk.CTkLabel(self.info_frame, text='Year | Type | Genre: -', font=('Arial', 15, 'bold'))
        self.year_type_genre_label.pack(pady=2, padx=15, anchor='w')

        self.runtime_label = ctk.CTkLabel(self.info_frame, text='Runtime: -', font=('Arial', 15, 'bold'))
        self.runtime_label.pack(pady=2, padx=15, anchor='w')

        self.rating_label = ctk.CTkLabel(self.info_frame, text='IMDb Rating: -', font=('Arial', 15, 'bold'))
        self.rating_label.pack(pady=2, padx=15, anchor='w')

        self.director_label = ctk.CTkLabel(self.info_frame, text='Director: -', font=('Arial', 15, 'bold'))
        self.director_label.pack(pady=2, padx=15, anchor='w')

        self.actors_label = ctk.CTkLabel(self.info_frame, text='Actors: -', font=('Arial', 15, 'bold'))
        self.actors_label.pack(pady=2, padx=15, anchor='w')

        self.language_country_label = ctk.CTkLabel(self.info_frame, text='Language | Country: -', font=('Arial', 15, 'bold'))
        self.language_country_label.pack(pady=2, padx=15, anchor='w')

        self.awards_label = ctk.CTkLabel(self.info_frame, text='Awards: -', font=('Arial', 15, 'bold'))
        self.awards_label.pack(pady=2, padx=15, anchor='w')

        # Plot scrollable
        self.plot_label = ctk.CTkLabel(self.info_frame, text='Plot:', font=('Arial', 15, 'bold'))
        self.plot_label.pack(pady=2, padx=15, anchor='w')
        self.plot_textbox = ctk.CTkTextbox(self.info_frame, width=400, height=85, font=('Arial', 15, 'normal'))
        self.plot_textbox.pack(pady=15, padx=15, fill='x')
        self.plot_textbox.configure(state='disabled')

        # Buttons
        self.fav_button_frame = ctk.CTkFrame(self, corner_radius=10)
        self.fav_button_frame.grid(row=2, column=0, pady=20, padx=20)
        self.add_fav_button = ctk.CTkButton(self.fav_button_frame, text='Add to Favorites', command=self.add_to_favorites, font=('Arial', 15, 'bold'))
        self.add_fav_button.grid(row=0, column=0, pady=5, padx=5)

        self.watch_button_frame = ctk.CTkFrame(self, corner_radius=10)
        self.watch_button_frame.grid(row=2, column=1, pady=20, padx=20)
        self.add_watch_button = ctk.CTkButton(self.watch_button_frame, text='Add to Watch', command=self.add_to_watch, font=('Arial', 15, 'bold'))
        self.add_watch_button.grid(row=2, column=1, pady=5, padx=5)

        # Open the movie's IMDb page when the poster is clicked
        self.poster_label.bind('<Button-1>', lambda event: webbrowser.open(self.imdb_url) if self.imdb_url else None)

        # Hover effect for poster
        self.poster_label.bind('<Enter>', lambda event: self.poster_label.configure(cursor='hand2') if self.imdb_url else None)
        self.poster_label.bind('<Enter>', lambda event: self.poster_frame.configure(fg_color='#545252') if self.imdb_url else None)
        self.poster_label.bind('<Leave>', lambda event: self.poster_label.configure(cursor='') if self.imdb_url else None)
        self.poster_label.bind('<Leave>', lambda event: self.poster_frame.configure(fg_color=('gray85', 'gray16')) if self.imdb_url else None)

    def update_movie(self, movie_data):
        self.current_movie = movie_data
        self.imdb_url = f"https://www.imdb.com/title/{movie_data['imdbID']}/"
        poster_url = movie_data.get('Poster')
        if poster_url and poster_url !='N/A':
            response = requests.get(poster_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((300, 400))
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(300, 400))
            self.poster_label.configure(image=ctk_image, text='')
            self.poster_label.image = ctk_image
        else:
            self.poster_label.configure(text='No Poster', image='', font=('Arial', 15, 'bold'), text_color='white')

        # Info
        self.title_label.configure(text=f"Title: {movie_data.get('Title', '-')}")
        self.year_type_genre_label.configure(
            text=f"{movie_data.get('Year', '-')}  |  {movie_data.get('Type', '-')}  |  {movie_data.get('Genre', '-')}"
        )
        self.runtime_label.configure(text=f"Runtime: {movie_data.get('Runtime', '-')}")
        self.rating_label.configure(text=f"IMDb Rating: {movie_data.get('imdbRating', '-')}")
        self.director_label.configure(text=f"Director: {movie_data.get('Director', '-')}")
        self.actors_label.configure(text=f"Actors: {movie_data.get('Actors', '-')}")
        self.language_country_label.configure(
            text=f"{movie_data.get('Language','-')}  |  {movie_data.get('Country', '-')}"
        )
        self.awards_label.configure(text=f"Awards: {movie_data.get('Awards', '-')}")
        self.plot_textbox.configure(state='normal')
        self.plot_textbox.delete('0.0', 'end')
        self.plot_textbox.insert('0.0', movie_data.get('Plot', '-'))
        self.plot_textbox.configure(state='disabled')

    def show_message(self, message):
        blank_image = Image.new("RGB", (300, 400), color=(30, 30, 30))
        ctk_blank = ctk.CTkImage(light_image=blank_image, dark_image=blank_image, size=(300, 400))
        self.poster_label.configure(image=ctk_blank, text=message, font=('Arial', 30, 'bold'), text_color='white')
        self.poster_label.image = ctk_blank
        self.imdb_url = None

        self.title_label.configure(text='Title: -')
        self.year_type_genre_label.configure(text='Year | Type | Genre: -')
        self.runtime_label.configure(text='Runtime: -')
        self.rating_label.configure(text='IMDb Rating: -')
        self.director_label.configure(text='Director: -')
        self.actors_label.configure(text='Actors: -')
        self.language_country_label.configure(text='Language | Country: -')
        self.awards_label.configure(text='Awards: -')
        self.plot_textbox.configure(state='normal')
        self.plot_textbox.delete('1.0', 'end')
        self.plot_textbox.configure(state='disabled')

    def add_to_favorites(self):
        if self.current_movie and self.add_callback:
            self.add_callback(self.current_movie)

    def add_to_watch(self):
        if self.current_movie and self.watch_callback:
            self.watch_callback(self.current_movie)