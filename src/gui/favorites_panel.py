import customtkinter as ctk
from ..utils import save_movie_list, load_movie_list

class FavoritesPanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.listbox = ctk.CTkTextbox(self, width=400, height=300)
        self.listbox.pack(padx=10, pady=10)
        self.refresh_list()

    def add_to_favorites(self, movie_data):
        save_movie_list('favorites.json', movie_data)
        self.refresh_list()

    def add_to_watch(self, movie_data):
        save_movie_list('to_watch.json', movie_data)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete('1.0', 'end')
        favorites = load_movie_list('favorites.json')
        to_watch = load_movie_list('to_watch.json')

        self.listbox.insert('1.0', 'Favorites:\n')
        for f in favorites:
            self.listbox.insert('end', f"- {f.get('Title')} {f.get('added_at')}\n")

        self.listbox.insert('end', '\nTo Watch:\n')
        for w in to_watch:
            self.listbox.insert('end', f"- {w.get('Title')} {w.get('added_at')}\n")

