# Welcome Screen
import tkinter as tk
from Data.colors import Colors
from multiprocessing.util import sub_debug


class Home:
    """Welcome message to the user & menu options to set up the game"""

    def __init__(self, window, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.TOP):
        self.frame= tk.Frame(master=window, name= "home", relief=relief, bg=bg_color)
        self.side=SIDE
        self.window=window
        self.bg_color=bg_color
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        welcome_message=tk.Label(self.frame, text="Welcome to FlashLingo!", font=("Century Gothic", 40, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        welcome_message.pack(side="top", pady=(250, 0))
        message2=tk.Label(self.frame, text="Press any button to continue...", font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        message2.pack(side="top", pady=55)

    # def click_any_button(self):