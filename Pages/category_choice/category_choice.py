# Choose your category

import tkinter as tk
from Data.colors import Colors
from Data.categories import Categories
from Widgets.Button.Button import Button


class CategoryChoice:
    """Second frame - it asks the user to choose a category to practice"""

    def __init__(self, window, controller, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.LEFT):
        self.frame = tk.Frame(master=window, name="home", relief=relief, bg=bg_color)
        self.side = SIDE
        self.bg_color = bg_color
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        choose_category=tk.Label(self.frame, text="What category do you want to practise today?",
                                 font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        choose_category.pack(side="top", pady=(100, 100))

        for key, value in Categories.items():
            button=Button(self.frame, key.lower(), key,
                 Colors.WHITE, Colors.BROWN, 20, 3,
                 handle_click=None,
                 padx=0, pady=5, side=tk.TOP)


# Need to work on what is below here!!!
    def handle_click(self, event):
        self.manage_button_colors(event)
        page_name = str(event.widget).split('.')[2]

        # self is left frame -> master = root
        # right frame is in children of master
        rightFrame = self.master.children['rightFrame']

        # destroy children
        RightFrame.destroy_children(rightFrame)

        # add new page -> page_name
        RightFrame.frame_content(rightFrame, page_name)

    def manage_button_colors(self, event):
        # clicked button -> event.widget
        # all the menu buttons -> event.widget.master.children
        for child in event.widget.master.winfo_children():
            if child == event.widget:
                child.configure(bg=Colors.BLACK, fg=Colors.WHITE)
            else:
                child.configure(bg=Colors.BROWN, fg=Colors.WHITE)

    def selected_button_color(self, button):
        # tk button configure
        button.configure(bg=Colors.BLACK, fg=Colors.WHITE)






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