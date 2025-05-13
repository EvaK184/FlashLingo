# import everything

from Widgets import Window, MainFrame

if __name__=="__main__":

    # Root Window
    root=Window("FlashLingo")

    MainFrame= MainFrame(window= root.window)

    # start window (mainloop())
    root.start_method()
