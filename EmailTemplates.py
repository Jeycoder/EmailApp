from distutils.util import execute
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import mysql.connector as mysql

window=Tk()
window.title("Email Templates")
window.geometry("700x700")
window["bg"] = "#FFF"

email_frame = Frame(window)
email_frame.pack()
label = Label(email_frame, text = "Email Templates",font="Calibri 14 bold")


#table Creation
table = ttk.Treeview(email_frame)
#Setting Columns  for the table
table["columns"] = ("Id","Name","Subject","Message")

table.column("#0", width=0,  stretch=NO)
table.column("Id",anchor=CENTER,width=80)
table.column("Name",anchor=CENTER,width=120)
table.column("Subject",anchor=CENTER,width=120)
table.column("Message",anchor=CENTER,width=120)


#Setting the Heading
table.heading("#0",text="",anchor=CENTER)
table.heading("Id",text="#",anchor=CENTER)
table.heading("Name",text="Name",anchor=CENTER)
table.heading("Subject",text="Subject",anchor=CENTER)
table.heading("Message",text="Message",anchor=CENTER)

def actualizar():
    dbconnection = mysql.connector(host="localhost",
    user="root",
    passwd="password123",
    database="python")


    try:
        data=name.get(),subject.get(),message.get()
        mycursor= dbconnection.cursor()
        mycursor=execute("UPDATE email_templates SET Name=?,Subject=?,Message=? WHERE Id="+ myID.get(),(data))
        dbconnection.commit()
    except:
        messagebox.showwarning("WARNING","An error has ocurred trying to update the list")

label.pack()
table.pack()

window.mainloop()