# import everything
import tkinter as tk
from Widgets import Window, MainFrame
from Pages import Home, CategoryChoice

if __name__=="__main__":

    # Root Window
    #root=Window("FlashLingo")
    root=tk.Tk("Flashlingo")
    Main=MainFrame(root)

    #Home= Home(window= root.window)

    #category_choice=CategoryChoice(window=root.window)




    # start window (mainloop())
    root.mainloop()