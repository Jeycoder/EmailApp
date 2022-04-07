from tkinter import *

class report_list():
    def __init__(self, root):
        new_window = Toplevel(root)
        new_window.geometry("400x400")
        new_window.wm_title("Report Email Lists")
        new_window.wait_visibility()
        new_window.grab_set_global()

        #wait until new window closes
        root.wait_window(new_window)
