from tkinter import *
from tkintertable import TableCanvas, TableModel
from PIL import Image, ImageTk  # Library to work with images as icons


class EmailTemplateView:
    def __init__(self, root, list_templates):
        self.listTemplates = list_templates
        self.root = root
        window = Toplevel(root)  # Make new windows in the toplevel of main window
        window.wm_title("Email Templates")
        window.geometry("800x400")

        email_frame = Frame(window)
        email_frame.pack()
        label = Label(email_frame, text="Email Templates", font="Calibri 14 bold")

        # table Creation
        model = TableModel()
        self.data_table(model)
        # table = ttk.Treeview(email_frame)
        self.table = TableCanvas(email_frame, model=model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=700)
        self.table.show()
        # Add ACtions buttons
        self.actions_table()

        label.grid(column=1, row=1)
        self.table.grid(column=1, row=1)

        # Button Add
        btn_add = Button(window, width=5, height=1, text="Add", command=self.addNewEmailTemplate)
        btn_add.pack()

        root.wait_window(window)  # wait until new window close

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
                data[index]['Image'] = row[4]
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
                x1, y1, x2, y2 = self.table.getCellCoords(0, 5)
                # Add button Delete
                btn_delete = Button(self.table, width=1, height=1, text="D")
                self.table.create_window(((x1 + 50), y1 + 1), anchor=NW, window=btn_delete)

                index += 1

            self.table.update()
        except Exception as e:
            print(str(e))

    # Window for add new template
    def addNewEmailTemplate(self):
        window = Toplevel(self.root)  # Make new windows in the toplevel of main window
        window.wm_title("New Email Template")
        window.geometry("350x350")

        # Variebles Storage
        self.txt_name = StringVar()
        self.txt_subject = StringVar()
        self.txt_message = StringVar()
        self.txt_img = StringVar()

        Label(window, text="New Email Templates", font="Calibri 14 bold").grid(pady=5, padx=65,
                                                                               column=2, row=1, sticky=E, columnspan=3)
        # label Name
        Label(window, text="Name").grid(pady=5,
                                        column=2, row=3, sticky=E)
        # texbox Name
        Entry(window, width=25, textvariable=self.txt_name).grid(padx=5,
                                                                 column=3, row=3, columnspan=2)

        # Label Subject
        Label(window, text="Subject").grid(pady=5,
                                           column=2, row=4, sticky=E)
        # texbox Subject
        Entry(window, width=25, textvariable=self.txt_subject).grid(padx=5,
                                                                    column=3, row=4, columnspan=2)

        # label Message
        Label(window, text="Message").grid(pady=5,
                                           column=2, row=5, sticky=E)
        # texbox Message

        Text(window, width=33, height=10).grid(padx=5,
                                               column=3, row=5, columnspan=2)

        # Label Image
        Label(window, text="Image").grid(
            column=2, row=8, sticky=E)
        # texbox Image

        Entry(window, width=15, textvariable=self.txt_img).grid(padx=5,
                                                                column=3, row=8)

        # Button Upload
        Button(window, width=5, height=1, text="upload").grid(padx=5,
                                                              column=4, row=8)

        # Button Save
        Button(window, width=5, height=1, text="Save").grid(
            column=1, row=9, columnspan=3, sticky=S)

        self.root.wait_window(window)  # wait until new window closes
