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
        self.frame2 = tk.Frame(master=master, name="home2", relief=relief, bg=bg_color)
        self.side = SIDE
        self.bg_color = bg_color
        self.master = master
        self.question = None
        self.answer_buttons = []
        self.chosen_answer = None
        self.word = None
        self.words = None
        self.optionsABCD = None
        self.index = 0
        self.score = 0
        self.next = None
        self.feedback = None
        self.end_msf = None
        self.back = None
        self.engVSbulg = None
        self.multi_choice()
        self.add_frame()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, minsize=250, weight=1)
        self.frame.grid_rowconfigure(0, minsize=225) #weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(0, weight=1)

    # What's below is work in progress....

    def multi_choice(self):
        category = self.master.category
        self.words = Categories[category]

        random.shuffle(self.words)
        self.score = 0
        self.engVSbulg = [self.questions, self.questions2]
        random.choice(self.engVSbulg)()

    def questions(self):
        self.word = self.words[self.index]
        self.question = tk.Label(self.frame, text=f"\nWhat is the English translation of {self.word['bulgarian']}?",
                             font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        self.question.grid(row = 0, column = 0, sticky = "nsew")

        options = [self.word['english']]

        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(self.words)
            if other_word["english"] not in options:
                options.append(other_word["english"])

        random.shuffle(options)

        self.optionsABCD = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}

        for i, (key, value) in enumerate(self.optionsABCD.items()):
            button=Button2(self.frame, key.lower(), value,
                 Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                 handle_click = self.choose_answer,
                 row = i+1, column = 0)
            self.answer_buttons.append(button)

    def choose_answer(self, event):
        self.chosen_answer = str(event.widget).split('.')[3].upper()
        for i in range(4):
            self.answer_buttons[i].button.destroy()
        if self.optionsABCD[self.chosen_answer] == self.word["english"]:
            self.feedback = tk.Label(self.frame2, text=f"Correct! And it is pronounced {self.word['pronunciation']}\n",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 0, column = 0, sticky = "n")
            self.score += 1
            self.next = Button2(self.frame2, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 0, column = 0, epady = (40,0))
        else:
            self.feedback = tk.Label(self.frame2, text=f"Wrong! The correct answer is '{self.word['english']}' and it is pronounced {self.word['pronunciation']}.",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 0, column = 0, pady = 0, sticky = "n")
            self.next = Button2(self.frame2, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 0, column = 0, epady = (80,0))

    def questions2(self):
        self.word = self.words[self.index]
        self.question = tk.Label(self.frame, text=f"\nWhat is the Bulgarian translation of {self.word['english']}?",
                             font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        self.question.grid(row = 0, column = 0, sticky = "nsew")

        options = [self.word['bulgarian']]

        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(self.words)
            if other_word["bulgarian"] not in options:
                options.append(other_word["bulgarian"])

        random.shuffle(options)

        self.optionsABCD = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}

        for i, (key, value) in enumerate(self.optionsABCD.items()):
            button=Button2(self.frame, key.lower(), value,
                 Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                 handle_click = self.choose_answer2,
                 row = i+1, column = 0)
            self.answer_buttons.append(button)

    def choose_answer2(self, event):
        self.chosen_answer = str(event.widget).split('.')[3].upper()
        for i in range(4):
            self.answer_buttons[i].button.destroy()
        if self.optionsABCD[self.chosen_answer] == self.word["bulgarian"]:
            self.feedback = tk.Label(self.frame2, text=f"Correct! And it is pronounced {self.word['pronunciation']}\n",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 0, column = 0, sticky = "n")
            self.score += 1
            self.next = Button2(self.frame2, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 0, column = 0, epady = (40,0))
        else:
            self.feedback = tk.Label(self.frame2, text=f"Wrong! The correct answer is '{self.word['bulgarian']}' and it is pronounced {self.word['pronunciation']}.",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
            self.feedback.grid(row = 0, column = 0, pady = 0, sticky = "n")
            self.next = Button2(self.frame2, "next", "Next",
                Colors.WHITE, Colors.BROWN, 12, 1,
                handle_click = self.next_question,
                row = 0, column = 0, epady = (80,0))

    def next_question(self, event):
        self.index += 1
        self.next.button.destroy()
        self.feedback.destroy()

        if self.index == 10:
            self.end_quiz()
        else:
            random.choice(self.engVSbulg)()

    def end_quiz(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.end_msf = tk.Label(self.frame, text=f"Quiz complete! Your score: {self.score}/10",
                                font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        self.end_msf.grid(row=0, column=0, sticky="nsew")
        self.back = Button2(self.frame, "back", "Back",
                            Colors.WHITE, Colors.BROWN, 20, 3,
                            handle_click=self.back_to_menu,
                            row=1, column=0, epady=(80, 0))

    def back_to_menu(self, event):
        self.frame.destroy()
        self.frame2.destroy()
        self.master.add_views()