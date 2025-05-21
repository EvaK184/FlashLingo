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
        self.question = None
        self.button = None
        self.chosen_answer = None
        self.word = None
        self.words = None
        self.optionsABCD = None
        self.index = 0
        self.score = 0
        self.next = None
        self.feedback = None
        self.end_msf = None
        self.multi_choice()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(7, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        for i in range(7):  # Suppose you have 3 rows
            self.frame.grid_rowconfigure(i, minsize=50)

    # What's below is work in progress....

    def multi_choice(self):
        category = self.master.category
        self.words = Categories[category]

        random.shuffle(self.words)
        self.score = 0
        self.questions()

    def questions(self):
        self.word = self.words[self.index]
        self.question = tk.Label(self.frame, text=f"\nWhat is the English translation of {self.word['bulgarian']}?",
                             font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        self.question.grid(row = 0, column = 0, sticky = "nsew")

        options = [self.word['english']]

        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(self.words)
            if other_word["english"] not in options:
                options.append(other_word["english"])

        random.shuffle(options)

        self.optionsABCD = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}

        for i, (key, value) in enumerate(self.optionsABCD.items()):
            self.button=Button2(self.frame, key.lower(), value,
                 Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                 handle_click = self.choose_answer,
                 row = i+1, column = 0)

    def choose_answer(self, event):
        self.chosen_answer = str(event.widget).split('.')[3].upper()
        if self.optionsABCD[self.chosen_answer] == self.word["english"]:
            self.feedback = tk.Label(self.frame, text=f"Correct! And it is pronounced {self.word['pronunciation']}\n",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 6, column = 0, sticky = "nsew")
            self.score += 1
            self.next = Button2(self.frame, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 6, column = 0, epady = (80,0))
        else:
            self.feedback = tk.Label(self.frame, text=f"Wrong! The correct answer is '{self.word['english']}' and it is pronounced {self.word['pronunciation']}.",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 6, column = 0, pady = 0, sticky = "nsew")
            self.next = Button2(self.frame, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 6, column = 0, epady = (160,0))

    def next_question(self, event):
        self.index += 1
        self.next.button.destroy()
        self.feedback.destroy()

        if self.index == 10:
            self.end_quiz()
        else:
            self.questions()

    def end_quiz(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.end_msf = tk.Label(self.frame, text=f"Quiz complete! Your score: {self.score}/10",
                                font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        self.end_msf.grid(row=0, column=0, sticky="nsew")
