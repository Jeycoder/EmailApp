import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class SendEmail(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Send Emails')
        self.geometry('300x400+400+200')

        # Main label
        self.label = ttk.Label(self,font=("Arial", 16), text='Send Emails')
        self.label.place(x=10, y=10)
        #controls
        self.lblEmails = ttk.Label(self, font=("Arial", 12), text='Email List')
        self.lblEmails.place(x=10,y=70)
        TEmailList = tk.Text(self, height=1, width=20,font=("Arial", 12))
        TEmailList.place(x=100,y=70)
        self.lblTemplate = ttk.Label(self, font=("Arial", 12), text='Template')
        self.lblTemplate.place(x=10, y=120)
        TTemplate = tk.Text(self, height=1, width=20, font=("Arial", 12))
        TTemplate.place(x=100, y=120)
        # button
        self.button = ttk.Button(self, text='Send')
        self.button['command'] = self.button_clicked
        self.button.place(x=10, y=330)
    def button_clicked(self):
        showinfo(title='Email Project',
                 message='Sent!')

    def Show(self):
        app = SendEmail()
        app.mainloop()
