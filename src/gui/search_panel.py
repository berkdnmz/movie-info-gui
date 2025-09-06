import customtkinter as ctk

class SearchPanel(ctk.CTkFrame):
    def __init__(self, master, search_callback, **kwargs):
        super().__init__(master, **kwargs)
        # Entry frame
        self.entry_frame = ctk.CTkFrame(self, corner_radius=10)
        self.entry_frame.grid(row=0, column=0, pady=15, padx=15, sticky='n')
        self.movie_entry = ctk.CTkEntry(self.entry_frame, width=390, font=('Arial', 15, 'roman'))
        self.movie_entry.grid(row=0, column=0, padx=5, pady=5)
        self.movie_entry.bind('<Return>', self.on_search)
        self.movie_entry.after(100, lambda :self.movie_entry.focus())

        # Search frame
        self.search_button_frame = ctk.CTkFrame(self, corner_radius=10)
        self.search_button_frame.grid(row=0, column=1, pady=15, padx=15, sticky='n')
        self.search_button = ctk.CTkButton(self.search_button_frame, text='Search', command=self.on_search, font=('Arial', 15, 'bold'))
        self.search_button.grid(row=0, column=0, padx=5, pady=5)

        self.search_callback = search_callback

    def on_search(self, event=None):
        movie_name = self.movie_entry.get()
        if movie_name:
            if self.search_callback:
                self.search_callback(movie_name)
                self.movie_entry.delete(0,ctk.END)