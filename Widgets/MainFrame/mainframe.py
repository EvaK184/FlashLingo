import tkinter as tk
from tkinter import *
from  Data.colors import Colors
from Pages import Home, CategoryChoice, LevelChoice

class MainFrame(tk.Frame):
    """ The main frame will be the parent for all the main pages/views and will control the navigation between them """

    def __init__(self, window, name = "mainframe"):
        super().__init__(
            master=window,
            name=name)
        self.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        self.add_views()

    def add_views(self):
        home = Home(self)
        home.frame.focus_set()
        home.frame.bind("<Key>",self.continue_action)

    def continue_action(self, event):
        category_choice = CategoryChoice(self)

    def on_category_chosen(self):
        level_choice = LevelChoice(self)