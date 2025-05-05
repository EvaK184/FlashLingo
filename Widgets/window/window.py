import tkinter as tk
from  Data.colors import Colors

class Window:
    """Creates the app's Window"""

    def __init__(self, title):
        self.window=tk.Tk()
        self.window.title(title)
        self.window.configure(bg=Colors.WHITE)
        self.set_size()
        

    def start_method(self):
        self.window.mainloop()

    def set_size(self):
        w= 1024
        h= 768
        self.window.geometry("%dx%d"%(w,h))