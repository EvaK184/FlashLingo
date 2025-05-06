import tkinter as tk
from  Data.colors import Colors
from Data.categories import Categories
from Widgets.Button.Button import Button

class Window(tk.Tk):
    """Creates the app's Window"""

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.configure(bg=Colors.WHITE)
        self.set_size()

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, CategoryChoice):
            frame = F(container, self)

            # initializing frame of that object from
            # Home, CategoryChoice respectively with
            # for loop
            self.frames[F] = frame

            frame.add_frame()

        self.show_frame(Home)

        # to display the current frame passed as
        # parameter

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def start_method(self):
        self.window.mainloop()

    def set_size(self):
        w= 1024
        h= 768
        self.geometry("%dx%d"%(w,h))

class Home:
    """Welcome message to the user & menu options to set up the game"""

    def __init__(self, window, controller, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.LEFT):
        self.frame= tk.Frame(master=window, name= "home", relief=relief, bg=bg_color)
        self.side=SIDE
        self.window=window
        self.bg_color=bg_color
        self.controller=controller
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        welcome_message=tk.Label(self.frame, text="Welcome to FlashLingo!", font=("Century Gothic", 40, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        welcome_message.pack(side="top", pady=(250, 0))
        message2=Button(self.frame, name = "continue", text="Continue", command=lambda : self.controller.show_frame(CategoryChoice))

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
            button=Button(self.frame, key.lower(), key, None,
                 Colors.WHITE, Colors.BROWN, 20, 3,
                 padx=0, pady=5)