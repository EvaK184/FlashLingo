# Quiz time!

import tkinter as tk
from Data.colors import Colors
from Widgets.Button.Button import Button
from Data.bulgarian import *
from Data.categories import Categories
import random

class QuizBeginner:

    def __init__(self, master, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.TOP):
        self.frame = tk.Frame(master=master, name="home", relief=relief, bg=bg_color)
        self.side = SIDE
        self.bg_color = bg_color
        self.master = master
        self.multi_choice()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    # What's below is work in progress....

    def multi_choice(self):
        category = self.master.category


        choose_category = tk.Label(self.frame, text="What level is your knowledge in this category?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        choose_category.pack(side="top", pady=(100, 100))

        levels = ("Beginner", "Intermediate", "Advanced")

        for level in levels:
            button=Button(self.frame, level.lower(), level,
                 Colors.WHITE, Colors.BROWN, 20, 3,
                 handle_click = None,
                 padx=0, pady=5, side=tk.TOP)

# from original
def multi_choice(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"\nWhat is the English translation of {word['bulgarian']}?")
        options = [word['english']]
        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(words)
            if other_word["english"] not in options:
                options.append(other_word["english"])
        random.shuffle(options)
        optionsABCD = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}
        user_answer = user_input(f"A.{options[0]} B.{options[1]} C.{options[2]} D.{options[3]}\n")
        if optionsABCD[user_answer] == word["english"]:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}' and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")