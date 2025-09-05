import customtkinter as ctk
from gui.search_panel import SearchPanel

def on_movie_search(movie_name):
    print(f"Searching for:{movie_name}")

def main():
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    root = ctk.CTk()
    root.title('Movie Info Dashboard')
    root.geometry('900x600')
    root.bind('<Escape>', lambda event: root.destroy())

    search_panel = SearchPanel(root, search_callback=on_movie_search)
    search_panel.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()