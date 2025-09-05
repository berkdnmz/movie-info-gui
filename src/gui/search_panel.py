import customtkinter as ctk

class SearchPanel(ctk.CTkFrame):
    def __init__(self, master, search_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.movie_entry = ctk.CTkEntry(self, width=300, placeholder_text='Enter movie title...')
        self.movie_entry.grid(row=0, column=0, padx=10, pady=10)
        self.movie_entry.bind('<Return>', self.on_search)
        self.movie_entry.after(100, lambda :self.movie_entry.focus())

        self.search_button = ctk.CTkButton(self, text='Search', command=self.on_search)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.search_callback = search_callback

    def on_search(self, event=None):
        movie_name = self.movie_entry.get()
        if movie_name:
            if self.search_callback:
                self.search_callback(movie_name)
                self.movie_entry.delete(0,ctk.END)