import tkinter as tk
from Data.colors import Colors

# Wrapper Class -> wrapped the tkinter.Button()
class Button:
    """It will create Tkinter Button."""
    def __init__(self, master, name, text, command,
                 fg=Colors.WHITE, bg=Colors.BROWN, width=20, height=3,

                 padx=0, pady=0, side=tk.TOP):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            command=command,
            width=width,
            height=height,
            activebackground=Colors.BLACK)
        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()

    def add_button(self):
        self.button.configure(font=('Arial', 12))
        self.button.pack(
            padx = self.padx,
            pady = self.pady,
            side = self.side)
