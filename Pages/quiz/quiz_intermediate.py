import tkinter as tk
from Data.colors import Colors
from Widgets.Button.Button import Button2
from Data.categories import Categories
import random

class QuizIntermediate:

    def __init__(self, master, bg_color=Colors.BLUE, relief=tk.SUNKEN):
        self.frame = tk.Frame(master=master, name="home", relief=relief, bg=bg_color)
        #self.frame2 = tk.Frame(master=master, name="home2", relief=relief, bg=bg_color)
        self.bg_color = bg_color
        self.master = master
        self.add_frame()
        self.words = None
        #self.engVSbulg = [self.questions, self.questions2]
        self.word = None
        self.index = 0
        self.score = 0
        self.answer_buttons = []
        self.answer_field = None
        self.chosen_answer = None
        self.feedback = None
        self.next = None
        self.BuildSentence()

    def add_frame(self):
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, minsize=250, weight=1)
        self.frame.grid_rowconfigure(0, minsize=225)
        self.frame.grid_columnconfigure(0, weight=1)

    def BuildSentence(self):
        category = self.master.category
        self.words = Categories[category]
        random.shuffle(self.words)
        #random.choice(self.engVSbulg)()
        self.questions()

    def questions(self):
        self.word = self.words[self.index]
        question = tk.Label(self.frame, text=f"\nWhat is the English translation of {self.word['bulgarian']}?",
                            font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        question.grid(row = 0, column = 0, sticky = "nsew")
        self.answer_field = tk.Text(self.frame, bg=Colors.BLUE, fg=Colors.BROWN, height=5, width=50, font=("Century Gothic", 15))
        self.answer_field.grid(row = 1, column = 0, sticky = "nsew")

        button=Button2(self.frame, "Submit", Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                       handle_click = self.choose_answer, row = 1, column = 1)

        options = [self.word['english']]

        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(self.words)
            if other_word["english"] not in options:
                options.append(other_word["english"])

        split_options = options[0].split(" ") + options[1].split(" ") + options[2].split(" ") + options[3].split(" ")
        random.shuffle(split_options) #shuffle the individual words from all the expressions

        for idx, i in enumerate(split_options):
            button=Button2(self.frame, i,
                           Colors.WHITE, Colors.BROWN, 20, 3, epady=4,
                           handle_click = self.build,
                           row = idx%8+2, column = idx//8)
            self.answer_buttons.append(button)


    def build(self, event):
        self.chosen_answer = event.widget.cget("text")
        self.answer_field.insert("end", self.chosen_answer+" ")

    def choose_answer(self, event):
        text_input = self.answer_field.get("1.0", "end -2 chars")
        for i in range(len(self.answer_buttons)):
            self.answer_buttons[i].button.destroy()
        if text_input == self.word["english"]:
            self.feedback = tk.Label(self.frame, text=f"Correct! And it is pronounced {self.word['pronunciation']}\n",
                                     font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color,
                                     wraplength=900)
            self.feedback.grid(row=2, column=0, sticky="n")
            self.score += 1
            self.next = Button2(self.frame, "Next",
                                Colors.WHITE, Colors.BROWN, 12, 1,
                                handle_click = self.next_question,
                                row = 3, column = 0, epady = (40,0))
        else:
            self.feedback = tk.Label(self.frame, text=f"Wrong! The correct answer is '{self.word['english']}' and it is pronounced {self.word['pronunciation']}.",
                                     font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color,
                                     wraplength=900)
            self.feedback.grid(row=2, column=0, pady=0, sticky="n")
            self.next = Button2(self.frame, "Next",
                                Colors.WHITE, Colors.BROWN, 12, 1,
                                handle_click = self.next_question,
                                row = 3, column = 0, epady = (80,0))

    def next_question(self, event):
        self.index += 1
        self.next.button.destroy()
        self.feedback.destroy()

        if self.index == 10:
            self.end_quiz()
        else:
            #random.choice(self.engVSbulg)()
            self.questions()

    def end_quiz(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.end_msg = tk.Label(self.frame, text=f"Quiz complete! Your score: {self.score}/10",
                                font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color, wraplength=900)
        self.end_msg.grid(row=0, column=0, sticky="nsew")
        self.back = Button2(self.frame, "Back",
                            Colors.WHITE, Colors.BROWN, 20, 3,
                            handle_click=self.back_to_menu,
                            row=1, column=0, epady=(80, 0))

    def back_to_menu(self, event):
        self.frame.destroy()
        self.master.add_views()

"""
        for i in range(len(self.answer_buttons)):
            self.answer_buttons[i].button.destroy()
            #In progress...

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
"""

# From Original Flashlingo
"""
def build(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"\nWhat is the Bulgarian translation of {word['english']}? (add spaces between the numbers if multiple numbers are needed for the correct answer)")
        options = [word['bulgarian']]
        while len(options) < 4:  # Add 3 other incorrect answers
            other_word = random.choice(words)
            if other_word["bulgarian"] not in options:
                options.append(other_word["bulgarian"])
        #make a list of individual words made out of 4 different expressions
        split_options = options[0].split(" ") + options[1].split(" ") + options[2].split(" ") + options[3].split(" ")
        random.shuffle(split_options) #shuffle the individual words from all of the expressions
        options_list = []
        for option in split_options:
            option_dict = {str(split_options.index(option)):option} #make a dictionary with the form {individual_word_index(as a string):individual_word}
            options_list.append(option_dict) #put all of the dictionaries together in a list
        for x in options_list:
            print(x)
        user_answer=user_input()
        user_answer = user_answer.split(" ") #make a list with each number in the user's answer
        user_answer2 = []
        for i in user_answer:
            user_answer2.append(options_list[int(i)][i])
        user_answer3=" ".join(user_answer2)
        print(user_answer3)
        if user_answer3 == word['bulgarian']:
            print(f"Correct! And it is pronounced {word['pronunciation']}\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['bulgarian']}' and it is pronounced {word['pronunciation']}.\n")
    print(f"Quiz complete! Your score: {score}/{len(words)}")
"""