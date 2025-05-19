import tkinter as tk
from doctest import master
from tkinter.constants import CENTER

from Data.colors import Colors

# Wrapper Class -> wrapped the tkinter.Button()
# Main Button class -> packed
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
            wraplength=200,
            justify=CENTER,
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

# Secondary Button class -> Gridded
class Button2:
    """It will create Tkinter Button."""
    def __init__(self, master, name, text,
                 fg, bg, width, height,
                 handle_click,
                 padx=0, pady=0, epadx=0, epady=0, row = 0, column = 0, side=tk.TOP):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=width,
            height=height,
            padx=padx,
            pady=pady,
            wraplength=200,
            justify=CENTER,
            activebackground=Colors.BLACK)
        self.master = master
        self.padx = padx
        self.pady = pady
        self.epadx = epadx
        self.epady = epady
        self.side = side
        self.row = row
        self.column = column
        self.add_button()
        self.bind_event(handle_click)   # bind the event handler

    def add_button(self):
        self.button.configure(font=('Arial', 12))
        self.button.grid(row = self.row, column = self.column, padx =self.epadx, pady = self.epady)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    # event binding to button
    def bind_event(self, handle_click):
        # in tkinter -> .bind() -> left mouse click -> <Button-1>
        self.button.bind('<Button-1>', handle_click)