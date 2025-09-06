import customtkinter as ctk
from .gui.search_panel import SearchPanel
from .gui.movie_detail_panel import MovieDetailPanel
from .api_handler import fetch_movie_data
from .gui.favorites_panel import FavoritesPanel

def main():
    def on_movie_search(movie_name):
        movie_data = fetch_movie_data(movie_name)
        if movie_data and movie_data.get('Response') == 'True':
            movie_detail_panel.update_movie(movie_data)
        else:
            print('Movie not found!')

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    root = ctk.CTk()
    root.title('Movie Info Dashboard')
    root.geometry('900x600')
    root.bind('<Escape>', lambda event: root.destroy())

    search_panel = SearchPanel(root, search_callback=on_movie_search)
    favorites_panel = FavoritesPanel(root)
    movie_detail_panel = MovieDetailPanel(
        root,
        add_callback=favorites_panel.add_to_favorites,
        watch_callback=favorites_panel.add_to_watch
    )
    search_panel.pack(pady=20)
    movie_detail_panel.pack(pady=20)
    favorites_panel.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
