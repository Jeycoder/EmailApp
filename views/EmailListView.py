import tkinter as tk
from tkinter import ttk, N, S,W,E
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview

class EmailListView:
    def __init__(self, root, list_views):
        super().__init__()

        # configure the root window
        self.title('Email List')
        self.geometry('600x400+400+200')

        # Main label
        self.label = ttk.Label(self,font=("Arial", 16), text='List of Emails')
        self.label.place(x=10, y=10)
        #controls
        tv = Treeview(self)
        tv['columns'] = ('Name', 'Emails', 'Action')
        tv.heading("#0", text='#', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Name', text='Name')
        tv.column('Name', anchor='center', width=100)
        tv.heading('Emails', text='No of Emails')
        tv.column('Emails', anchor='center', width=100)
        tv.heading('Action', text='Action')
        tv.column('Action', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def Show(self):
        app = EmailListView()
        app.mainloop()