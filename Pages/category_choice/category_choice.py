# Choose your category

import tkinter as tk
from Data.colors import Colors
from Data.categories import Categories
from Widgets.Button.Button import Button


class CategoryChoice:
    """Second frame - it asks the user to choose a category to practice"""

    def __init__(self, master, bg_color=Colors.BLUE, relief=tk.SUNKEN, side=tk.TOP):
        self.frame = tk.Frame(master=master, name="category_choice", relief=relief, bg=bg_color)
        self.master = master
        self.side = side
        self.bg_color = bg_color
        self.chosen_category = None
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def frame_content(self):
        choose_category=tk.Label(self.frame, text="What category do you want to practise today?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        choose_category.pack(side="top", pady=(100, 100))

        for key, value in Categories.items():
            button=Button(self.frame, key.lower(), key,
                          Colors.WHITE, Colors.BROWN, 20, 3,
                          handle_click = self.choose_category,
                          padx=0, pady=5, side=tk.TOP)

    def choose_category(self, event):
        self.chosen_category = str(event.widget).split('.')[3]
        self.master.on_category_chosen()