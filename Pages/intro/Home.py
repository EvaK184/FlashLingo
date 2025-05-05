# Welcome Screen
import tkinter as tk
from Data.colors import Colors
from multiprocessing.util import sub_debug


class Home:
    """Welcome message to the user & menu options to set up the game"""

    def __init__(self, window, bg_color=Colors.BLUE, relief=tk.SUNKEN, SIDE=tk.LEFT):
        self.frame= tk.Frame(master=window, name= "home", relief=relief, bg=bg_color)
        self.side=SIDE
        self.window=window
        self.bg_color=bg_color
        self.frame_content()
        self.add_frame()
        self.bind_event()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        welcome_message=tk.Label(self.frame, text="Welcome to FlashLingo!", font=("Century Gothic", 40, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        welcome_message.pack(side="top", pady=(250, 0))
        message2=tk.Label(self.frame, text="Press Enter to start the quiz...", font=("Century Gothic", 25, "bold"), fg=Colors.BROWN, bg=self.bg_color)
        message2.pack(side="top", pady=55)

    # Provisional Code. May not work

    # event binding to an action
    def bind_event(self):
        # in tkinter -> .bind() -> left mouse click -> <Button-1>
        self.frame.bind('<Return>', self.switch_frames())

    def switch_frames(self):
        self.frame.pack_forget()





def handle_click(self, event):
    page_name = str(event.widget).split('.')[2]
    # self is left frame -> master = root
    # right frame is in children of master
    rightFrame = self.master.children['rightFrame']

    # destroy children
    RightFrame.destroy_children(rightFrame)

    # add new page -> page_name
    RightFrame.frame_content(rightFrame, page_name)

