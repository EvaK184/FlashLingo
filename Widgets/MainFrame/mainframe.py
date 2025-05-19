import tkinter as tk
from tkinter import *
from  Data.colors import Colors
from Pages import Home, CategoryChoice, LevelChoice, QuizBeginner

class MainFrame(tk.Frame):
    """ The main frame will be the parent for all the main pages/views and will control the navigation between them """

    def __init__(self, window, name = "mainframe"):
        super().__init__(
            master=window,
            name=name)
        self.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        self.add_views()
        self.category_choice = None
        self.category = None
        self.level_choice = None
        self.level = None

    def add_views(self):
        home = Home(self)
        home.frame.focus_set()
        home.frame.bind("<Key>",self.continue_action)

    def continue_action(self, category_choice):
        self.category_choice = CategoryChoice(self)

    def on_category_chosen(self):
        self.category = self.category_choice.chosen_category.capitalize()
        self.level_choice = LevelChoice(self)

    def start_quiz(self):
        self.level = self.level_choice.chosen_level
        quiz = QuizBeginner(self)