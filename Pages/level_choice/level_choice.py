# Choose your level

import tkinter as tk
from Data.colors import Colors
from Widgets.Button.Button import Button


class LevelChoice:
    """Third frame - it asks the user to say what level is their knowledge in this category"""

    def __init__(self, master, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.TOP):
        self.frame = tk.Frame(master=master, name="home", relief=relief, bg=bg_color)
        self.side = SIDE
        self.bg_color = bg_color
        self.master = master
        self.chosen_level = None
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def frame_content(self):
        choose_category=tk.Label(self.frame, text="What level is your knowledge in this category?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        choose_category.pack(side="top", pady=(100, 100))

        levels = ("Beginner", "Intermediate", "Advanced")

        for level in levels:
            button=Button(self.frame, level.lower(), level,
                 Colors.WHITE, Colors.BROWN, 20, 3,
                 handle_click = self.choose_level,
                 padx=0, pady=5, side=tk.TOP)

    def choose_level(self, event):
        self.chosen_level = str(event.widget).split('.')[3]
        self.master.start_quiz()