import tkinter as tk
from  Data.colors import Colors
from Data.categories import Categories
from Widgets.Button.Button import Button

class MainFrame():
    def __init__(self, master):
        mainframe=tk.Frame(master)
        mainframe.pack(padx=0, pady=0, fill="both", expand=True)
        self.index=0

        self.frameList = [Home(mainframe), CategoryChoice(mainframe)]
        self.frameList[1].forget()

    def changeWindow(self):
        self.frameList[self.index].forget()
        self.index=(self.index+1)%len(self.frameList)
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(side=self.side, fill=tk.BOTH, expand=True)


class Home(tk.Frame):
    """Welcome message to the user & menu options to set up the game"""

    def __init__(self, window, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.LEFT):
        super().__init__(window)
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
        message2=tk.Button(self.frame, text="Continue", fg=Colors.BROWN, bg=self.bg_color, command=MainFrame.changeWindow)
        message2.pack(side="top", pady=55)


class CategoryChoice(tk.Frame):
    """Second frame - it asks the user to choose a category to practice"""

    def __init__(self, window, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.LEFT):
        super().__init__(window)
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

        message2 = tk.Button(self.frame, text="Back", fg=Colors.BROWN, bg=self.bg_color,
                             command=MainFrame.changeWindow)
        message2.pack(side="top", pady=20)