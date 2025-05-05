import tkinter as tk
from Data.colors import Colors

# Wrapper Class -> wrapped the tkinter.Button()
class Button:
    """It will create Tkinter Button."""
    def __init__(self, master, name, text,
                 fg, bg, width, height,
                 handle_click,
                 padx=0, pady=0, side=tk.TOP):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=width,
            height=height,
            activebackground=Colors.BLACK)
        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()
        # bind the event handler
        self.bind_event(handle_click)

    def add_button(self):
        self.button.configure(font=('Arial', 12))
        self.button.pack(
            padx = self.padx,
            pady = self.pady,
            side = self.side)

    # event binding to button
    def bind_event(self, handle_click):
        # in tkinter -> .bind() -> left mouse click -> <Button-1>
        self.button.bind('<Button-1>', handle_click)
