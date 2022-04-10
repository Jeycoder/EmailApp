from tkinter import *
from tkinter import ttk
from tkintertable import TableCanvas, TableModel
from PIL import  Image, ImageTk  #Library to work with images as icons
class EmailTemplateView:
    def __init__(self, root, list_templates):
        self.listTemplates = list_templates
        window = Toplevel(root)  # Make new windows in the toplevel of main window
        window.wm_title("Email Templates")
        window.geometry("700x300")

        # myID = StringVar()
        # Vname = StringVar()
        # Vsubject = StringVar()
        # Vmessage = StringVar()
        # Vimage = StringVar()

        email_frame = Frame(window)
        email_frame.pack()
        label = Label(email_frame, text="Email Templates", font="Calibri 14 bold")

        # table Creation
        # Setting Columns to the table
        model = TableModel()
        self.data_table(model)
        #table = ttk.Treeview(email_frame)
        table = TableCanvas(email_frame, model= model, cellbackgr='#e3f698', read_only=True)
        table.show()

        label.grid(column=1, row=1)
        table.grid(column=1, row = 1)
        #Button Add
        btn_add = Button(window, width=5, height=1, text="Add")
        btn_add.pack(side=RIGHT)

        window.wait_visibility()
        window.grab_set_global()
        # wait until new window closes
        root.wait_window(window)

    # CLICK SELECTOR
    def clickSelector(self, event):
        self.item = self.table.identify("item", event.x, event.y)
        self.myID.set(self.table.item(self.item, "values")[0])
        self.Vname.set(self.table.item(self.item, "values")[1])
        self.Vsubject.set(self.table.item(self.item, "values")[2])
        self.Vmessage.set(self.table.item(self.item, "values")[3])

    def data_table(self, model):
        #data = self.table.get_children()
        #for element in data:
         #   self.table.delete(element)
        try:
            data = dict()

            index = 0
            for row in self.listTemplates:
                #Add new actions images
                edit_image = PhotoImage(file="assets/icon_edit.png")
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Subject'] = row[2]
                data[index]['Message'] = row[3]
                index+=1

            model.importDict(data)
        except :
            print("Error Retreiving data")
