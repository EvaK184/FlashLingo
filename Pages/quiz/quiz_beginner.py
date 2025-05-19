# Quiz time!

import tkinter as tk
from Data.colors import Colors
from Widgets.Button.Button import Button2
from Data.bulgarian import *
from Data.categories import Categories
import random

class QuizBeginner:

    def __init__(self, master, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.TOP):
        self.frame = tk.Frame(master=master, name="home", relief=relief, bg=bg_color)
        self.side = SIDE
        self.bg_color = bg_color
        self.master = master
        self.chosen_answer = None
        self.word = None
        self.optionsABCD = None
        self.score = 0
        self.multi_choice()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    # What's below is work in progress....

    def multi_choice(self):
        category = self.master.category
        words = Categories[category]

        random.shuffle(words)
        self.score = 0

        for self.word in words:
            question = tk.Label(self.frame, text=f"\nWhat is the English translation of {self.word['bulgarian']}?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
            question.grid(row = 0, column = 0, sticky = "nsew")
            self.frame.grid_rowconfigure(7, weight=1)
            self.frame.grid_columnconfigure(0, weight=1)

            options = [self.word['english']]

            while len(options) < 4:  # Add 3 other incorrect answers
                other_word = random.choice(words)
                if other_word["english"] not in options:
                    options.append(other_word["english"])

            random.shuffle(options)

            self.optionsABCD = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}

            for i, (key, value) in enumerate(self.optionsABCD.items()):
                button=Button2(self.frame, key.lower(), value,
                     Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                     handle_click = self.choose_answer,
                     row = i+1, column = 0)

    def choose_answer(self, event):
        self.chosen_answer = str(event.widget).split('.')[3].upper()
        if self.optionsABCD[self.chosen_answer] == self.word["english"]:
            feedback = tk.Label(self.frame, text=f"Correct! And it is pronounced {self.word['pronunciation']}\n",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            feedback.grid(row = 6, column = 0, sticky = "nsew")
            self.score += 1
            next = Button2(self.frame, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 6, column = 0, epady = (80,0))
        else:
            feedback = tk.Label(self.frame, text=f"Wrong! The correct answer is '{self.word['english']}' and it is pronounced {self.word['pronunciation']}.",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            feedback.grid(row = 6, column = 0, pady = 0, sticky = "nsew")
            next = Button2(self.frame, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 6, column = 0, epady = (160,0))

    def next_question(self, event):
        pass


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