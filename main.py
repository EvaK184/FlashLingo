# import everything

from Widgets import Window
from Pages import Home, CategoryChoice

if __name__=="__main__":

    # Root Window
    root=Window("FlashLingo")

    Home= Home(window= root.window)

    #category_choice=CategoryChoice(window=root.window)




    # start window (mainloop())
    root.start_method()
