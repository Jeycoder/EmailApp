import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class NewTemplateWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('New Template')
        self.geometry('300x400+400+200')


        # Main label
        self.label = ttk.Label(self,font=("Arial", 16), text='New Email Template')
        self.label.place(x=10, y=10)

        self.lblName = ttk.Label(self, font=("Arial", 12), text='Name')
        self.lblName.place(x=10,y=70)
        TName = tk.Text(self, height=1, width=20,font=("Arial", 12))
        TName.place(x=100,y=70)
        self.lblSubject = ttk.Label(self, font=("Arial", 12), text='Subject')
        self.lblSubject.place(x=10, y=120)
        TSubject = tk.Text(self, height=1, width=20, font=("Arial", 12))
        TSubject.place(x=100, y=120)
        self.lblMessage = ttk.Label(self, font=("Arial", 12), text='Message')
        self.lblMessage.place(x=10, y=170)
        TMessage = tk.Text(self, height=5, width=20, font=("Arial", 12))
        TMessage.place(x=100, y=170)
        self.lblImage = ttk.Label(self, font=("Arial", 12), text='Attachment')
        self.lblImage.place(x=10, y=290)
        TImage = tk.Text(self, height=1, width=20, font=("Arial", 12))
        TImage.place(x=100, y=290)
        # button
        self.button = ttk.Button(self, text='Save')
        self.button['command'] = self.button_clicked
        self.button.place(x=10, y=330)

    def button_clicked(self):
        showinfo(title='Email Project',
                 message='Submitted!')

    def Show(self):
        app = NewTemplateWindow()
        app.mainloop()

