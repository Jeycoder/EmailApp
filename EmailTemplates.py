from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import mysql.connector

window = Tk()
window.title("Email Templates")
window.geometry("700x700")

myID = StringVar()
Vname = StringVar()
Vsubject = StringVar()
Vmessage = StringVar()
Vimage = StringVar()

email_frame = Frame(window)
email_frame.pack()
label = Label(email_frame, text="Email Templates", font="Calibri 14 bold")

# table Creation
table = ttk.Treeview(email_frame)
# Setting Columns  for the table
table["columns"] = ("Id", "Name", "Subject", "Message", "Image")

table.column("#0", width=0, stretch=NO)
table.column("Id", anchor=CENTER, width=80)
table.column("Name", anchor=CENTER, width=120)
table.column("Subject", anchor=CENTER, width=120)
table.column("Message", anchor=CENTER, width=120)
table.column("Image", anchor=CENTER, width=120)

# Setting the Heading
table.heading("#0", text="", anchor=CENTER)
table.heading("Id", text="#", anchor=CENTER)
table.heading("Name", text="Name", anchor=CENTER)
table.heading("Subject", text="Subject", anchor=CENTER)
table.heading("Message", text="Message", anchor=CENTER)
table.heading("Image", text="Image", anchor=CENTER)

#CLICK SELECTOR
def clickSelector(event):
    item = table.identify("item",event.x,event.y)
    myID.set(table.item(item,"text"))
    Vname.set(table.item(item,"values")[0])

table.bind("<Double-1>",clickSelector)

# SHOW TABLE
def show():
    dbconnection = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="python")
    mycursor = dbconnection.cursor()
    data = table.get_children()
    for element in data:
        table.delete(element)
    try:
        mycursor.execute("SELECT * FROM email_template")
        for row in mycursor:
            table.insert("", "end", iid=row[0], values=(row[0], row[1], row[2],row[3],row[4]))
    except mysql.connector.Error as error:
        print("Failed to show record into the table {}".format(error))


# UPDATE TABLE
def add():
    dbconnection = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="python")

    try:
        data = Vname.get(), Vsubject.get(), Vmessage.get()
        mycursor = dbconnection.cursor()
        mycursor.execute("INSERT INTO email_template(Name,Subject,Message) VALUES (%s,%s,%s)",data)
        dbconnection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
        messagebox.showwarning("WARNING", "An error has ocurred trying to Insert the list")
        pass
    show()


# UPDATE TABLE
def update():
    dbconnection = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="python")

    try:
        data = Vname.get(), Vsubject.get(), Vmessage.get()
        mycursor = dbconnection.cursor()
        mycursor.execute("UPDATE email_template SET Name=%s,Subject=%s,Message=%s WHERE Id=" + myID.get(), (data))
        dbconnection.commit()
    except:
        messagebox.showwarning("WARNING", "An error has ocurred trying to update the list")
        pass
    show()


# DELETE TABLE
def delete():
    dbconnection = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="python")
    mycursor = dbconnection.cursor()

    try:
        if messagebox.askyesno(message="Are you sure you want to delete the row selected?", title="WARNING"):
            mycursor.execute("DELETE FROM email_template  WHERE Id=" + myID.get())
        dbconnection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
    show()


e1 = Entry(email_frame, textvariable=myID)

labelName = Label(window, text="Name")
labelName.place(x=50, y=300)
e2 = Entry(window, textvariable=Vname, width=50)
e2.place(x=100, y=300)

labelSubject = Label(window, text="Subject")
labelSubject.place(x=50, y=330)
e2 = Entry(window, textvariable=Vsubject)
e2.place(x=100, y=330)

labelMessage = Label(window, text="Message")
labelMessage.place(x=50, y=380)
e2 = Entry(window, textvariable=Vmessage, width=50)
e2.place(x=100, y=380)

buttonAdd = Button(window, text="Add Template", command=add)
buttonAdd.place(x=50, y=420)

buttonShow = Button(window, text="show Template", command=show)
buttonShow.place(x=50, y=450)

buttonDelete = Button(window, text="Delete Template", command=delete)
buttonDelete.place(x=50, y=490)


label.pack()
table.pack()

window.mainloop()
