from tkinter import *
from tkinter import ttk
from tkintertable import TableCanvas, TableModel
from PIL import Image, ImageTk  # Library to work with images as icons


class EmailTemplateView:
    def __init__(self, root, list_templates):
        self.listTemplates = list_templates
        self.root = root
        window = Toplevel(root)  # Make new windows in the toplevel of main window
        window.wm_title("Email Templates")
        window.geometry("700x300")

        email_frame = Frame(window)
        email_frame.pack()
        label = Label(email_frame, text="Email Templates", font="Calibri 14 bold")

        # table Creation
        model = TableModel()
        self.data_table(model)
        # table = ttk.Treeview(email_frame)
        self.table = TableCanvas(email_frame, model=model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=525)
        self.table.show()
        # Add ACtions buttons
        self.actions_table()

        label.grid(column=1, row=1)
        self.table.grid(column=1, row=1)

        # Button Add
        btn_add = Button(window, width=5, height=1, text="Add")
        btn_add.pack(side=RIGHT)

        # Button Upload
        btn_upload = Button(window, width=5, height=1, text="Upload")
        btn_upload.pack(side=RIGHT)

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
        try:
            data = dict()
            index = 0
            for row in self.listTemplates:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Subject'] = row[2]
                data[index]['Message'] = row[3]
                data[index]['Actions'] = ''
                index += 1
            model.importDict(data)
        except Exception as e:
            print(str(e))

    def actions_table(self):
        try:
            index = 0
            for row in self.listTemplates:
                # Add new actions images
                edit_image = PhotoImage(file="assets/icon_edit.png")
                # Add button Edit
                btn_edit = Button(self.table, width=1, height=1, text="E")
                x1, y1, x2, y2 = self.table.getCellCoords(0, 4)
                self.table.create_window(((x1 + 1), y1 + 1), anchor=NW, window=btn_edit)

                # Add button Delete
                btn_delete = Button(self.table, width=1, height=1, text="D")
                self.table.create_window(((x1 + 50), y1 + 1), anchor=NW, window=btn_delete)

                index += 1

            self.table.update()
        except Exception as e:
            print(str(e))
