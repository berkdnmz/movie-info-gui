import customtkinter as ctk
from ..utils import save_movie_list, load_movie_list

class FavoritesPanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.fav_listbox_frame = ctk.CTkFrame(self, corner_radius=10)
        self.fav_listbox_frame.grid(row=0, column=0, sticky='n', pady=15, padx=15)
        self.fav_listbox = ctk.CTkTextbox(self.fav_listbox_frame, width=381, height=120, font=('Consolas', 15, 'normal'))
        self.fav_listbox.grid(row=0, column=0, padx=5, pady=5, sticky='n')

        self.watch_listbox_frame = ctk.CTkFrame(self, corner_radius=10)
        self.watch_listbox_frame.grid(row=0, column=1, sticky='n', pady=15, padx=15)
        self.watch_listbox = ctk.CTkTextbox(self.watch_listbox_frame, width=381, height=120, font=('Consolas', 15, 'normal'))
        self.watch_listbox.grid(row=0, column=0, pady=5, padx=5)
        self.refresh_list()

    def add_to_favorites(self, movie_data):
        save_movie_list('favorites.json', movie_data)
        self.refresh_list()

    def add_to_watch(self, movie_data):
        save_movie_list('to_watch.json', movie_data)
        self.refresh_list()

    def refresh_list(self):
        self.fav_listbox.delete('1.0', 'end')
        self.watch_listbox.delete('1.0', 'end')
        favorites = load_movie_list('favorites.json')
        to_watch = load_movie_list('to_watch.json')

        # Dates are saved in CSV. Only titles are displayed for clarity.
        spaces = "═" * 14
        self.fav_listbox.insert('2.0', f" {spaces}║  FAVORITES  ║{spaces}\n\n")
        for f in favorites:
            self.fav_listbox.insert('end', f"• {f.get('Title')}\n")

        self.watch_listbox.insert('end', F'  {spaces}║  TO WATCH  ║{spaces} \n\n')
        for w in to_watch:
            self.watch_listbox.insert('end', f"• {w.get('Title')}\n")

