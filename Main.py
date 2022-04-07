from tkinter import *
from MainMenu import MainMenu #class MainMenu


def main():
    window = Tk()  # GUI Application
    window.title('Send Emails Application')  # Set title in window
    window.geometry("500x500")
    app = MainMenu(window)
    app.pack()
    #Show window
    window.mainloop()

#Method to add a new window from menu click


#Call Main method
main()