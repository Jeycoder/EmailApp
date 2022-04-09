from ast import Name
from cgitb import text
from distutils.util import execute
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import mysql.connector 

window=Tk()
window.title("Email Templates")
window.geometry("700x700")
window["bg"] = "#FFF"

myID = StringVar();
Vname = StringVar()
Vsubject = StringVar()
Vmessage = StringVar()
Vimage = StringVar()

email_frame = Frame(window)
email_frame.pack()
label = Label(email_frame, text = "Email Templates",font="Calibri 14 bold")


#table Creation
table = ttk.Treeview(email_frame)
#Setting Columns  for the table
table["columns"] = ("Id","Name","Subject","Message","Image")

table.column("#0", width=0,  stretch=NO)
table.column("Id",anchor=CENTER,width=80)
table.column("Name",anchor=CENTER,width=120)
table.column("Subject",anchor=CENTER,width=120)
table.column("Message",anchor=CENTER,width=120)
table.column("Image",anchor=CENTER,width=120)



#Setting the Heading
table.heading("#0",text="",anchor=CENTER)
table.heading("Id",text="#",anchor=CENTER)
table.heading("Name",text="Name",anchor=CENTER)
table.heading("Subject",text="Subject",anchor=CENTER)
table.heading("Message",text="Message",anchor=CENTER)
table.heading("Image",text="Image",anchor=CENTER)

#SHOW TABLE
def show():
    dbconnection = mysql.connector(host="localhost",
    user="root",
    password="root",
    database="python")
    mycursor= dbconnection.cursor()
    data =table.get_children()
    for element in data:
        table.delete(element)
    try:
        mycursor.execute("SELECT * FROM email_template")
        for row in mycursor:
            table.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
    except:
        pass

#UPDATE TABLE
def update():
    dbconnection = mysql.connector(host="localhost",
    user="root",
    password="root",
    database="python")

    try:
        data=Vname.get(),Vsubject.get(),Vmessage.get()
        mycursor= dbconnection.cursor()
        mycursor.execute("UPDATE email_templates SET Name=?,Subject=?,Message=? WHERE Id="+ myID.get(),(data))
        dbconnection.commit()
    except:
        messagebox.showwarning("WARNING","An error has ocurred trying to update the list")
        pass
    show()

#DELETE TABLE
def delete():
    dbconnection = mysql.connector(host="localhost",
    user="root",
    password="root",
    database="python")
    mycursor= dbconnection.cursor()

    try:
        if messagebox.askyesno(message="Are you sure you want to delete the row selected?",title="WARNING"):
            mycursor.execute("DELETE FROM email_templates  WHERE Id="+ myID.get(),(data))
        dbconnection.commit()
    except:
        messagebox.showwarning("WARNING","An error has ocurred trying to update the list")
        pass
    show()

e1 = Entry(email_frame,textvariable=myID)

labelName=Label(email_frame,text="Name")
labelName.place(x=50,y=10)
e2=Entry(email_frame,textvariable=Vname,width=50)
e2.place(x=100,y=10)

labelSubject=Label(email_frame,text="Subject")
labelSubject.place(x=50,y=40)
e2=Entry(email_frame,textvariable=Vsubject)
e2.place(x=100,y=40)

labelMessage=Label(email_frame,text="Message")
labelMessage.place(x=280,y=40)
e2=Entry(email_frame,textvariable=Vmessage,width=50)
e2.place(x=320,y=40)



label.pack()
table.pack()

window.mainloop()