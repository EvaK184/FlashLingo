# Choose your category

import tkinter as tk
from Data.colors import Colors
from Data.categories import Categories
from Widgets.Button.Button import Button


class CategoryChoice:
    """Second frame - it asks the user to choose a category to practice"""

    def __init__(self, window, chosen_category = None, chose = False, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.TOP):
        self.frame = tk.Frame(master=window, name="home", relief=relief, bg=bg_color)
        self.window = window
        self.side = SIDE
        self.bg_color = bg_color
        self.frame_content()
        self.add_frame()
        self.chosen_category = chosen_category
        self.chose = chose

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        choose_category=tk.Label(self.frame, text="What category do you want to practise today?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        choose_category.pack(side="top", pady=(100, 100))

        for key, value in Categories.items():
            button=Button(self.frame, key.lower(), key,
                          Colors.WHITE, Colors.BROWN, 20, 3,
                          handle_click = self.choose_category,
                          padx=0, pady=5, side=tk.TOP)

    # Need to work on what is below here!!!
    def choose_category(self, event):
        self.chosen_category = str(event.widget).split('.')[2]
        self.chose = True


def main():
    choice = input(
        "What category do you want to practise today? Your options are:\na - Greetings\nb - Introducing yourself\nc - Numbers\nd - Days, Months and Seasons\ne - Telling the Time\n")
    words = Categories[choice]
    level = input("What level are you in this category? Press 'b' for begginer or 'i' for intermediate.")
    if level == "i":
        exercises = [build, quiz_user]
        random.choice(exercises)(words)
    if level == "b":
        exercises = [multi_choice, multi_choice2]
        random.choice(exercises)(words)

if __name__ == "__main__":
    main()