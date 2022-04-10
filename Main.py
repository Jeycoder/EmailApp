from tkinter import *
from views.MainMenuView import MainMenu #class MainMenu


def main():
    window = Tk()  # GUI Application
    window.title('Send Emails Application')  # Set title in window
    window.geometry("900x800")
    app = MainMenu(window)
    app.pack()
    #Show window
    window.mainloop()

#Call Main method
main()