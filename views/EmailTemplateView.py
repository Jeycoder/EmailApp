import io
import tkinter.messagebox
from tkinter import *
from tkinter.messagebox import showinfo
from tkintertable import TableCanvas, TableModel
from PIL import Image, ImageTk  # Library to work with images as icons
from tkinter import filedialog
from tkinter.filedialog import askopenfile

class EmailTemplateView:
    img = None
    def __init__(self, controller: object, root: object) -> object:
        self.model = None
        self.table = None
        self.controller = controller
        self.root = root
        window = Toplevel(root)  # Make new windows in the toplevel of main window
        window.wm_title("Email Templates")
        window.geometry("800x550")

        self.email_frame = Frame(window)
        self.email_frame.pack()
        label = Label(window, text="Email Templates", font="Calibri 14 bold")

        self.main_table()

        label.place(x=350, y=10)
        # Button Add
        btn_add = Button(window, width=5, height=1, text="Add", command=self.add_new_email_template)
        btn_add.place(x=350,y=450)

        root.wait_window(window)  # wait until new window close


    def main_table(self):
        # table Creation
        self.model = TableModel()
        self.data_table()
        self.table = TableCanvas(self.email_frame, model=self.model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=630, height=300)
        # Add data to the table
        self.table.model = self.model
        self.table.createTableFrame()
        # Show Table
        self.email_frame.place(x=50, y=50)
        self.table.show()

        # Add ACtions buttons
        self.actions_table()

    def data_table(self):
        try:
            data = dict()
            index = 0
            list_templates = self.controller.fetchAllController()
            for row in list_templates:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Subject'] = row[2]
                data[index]['Message'] = row[3]
                data[index]['Actions'] = ''
                index += 1
            self.model.importDict(data)
        except Exception as e:
            print(str(e))

    def actions_table(self):
        try:
            index = 0
            list_templates = self.controller.fetchAllController()
            for row in list_templates:
                # Add new actions images
                edit_image = PhotoImage(file="assets/icon_edit.png")
                # Add button Edit
                #btn_edit = Button(self.table, width=1, height=1, text="E", command = lambda idt=row[0] : self.edit_email_template(idt))
                x1, y1, x2, y2 = self.table.getCellCoords(index, 4)
                #self.table.create_window(((x1 + 1), y1 + 1), anchor=NW, window=btn_edit)

                # Add button Delete
                btn_delete = Button(self.table, width=1, height=1, text="D", command = lambda idt=row[0] : self.delete_email_template(idt))
                self.table.create_window(((x1 + 50), y1 + 1), anchor=NW, window=btn_delete)

                index += 1

            self.table.update()
        except Exception as e:
            print(str(e))

    #Window for add new template
    def add_new_email_template(self):
        window = Toplevel(self.root)  # Make new windows in the toplevel of main window
        window.wm_title("New Email Template")
        window.geometry("350x350")

        Label(window, text="New Email Template", font="Calibri 14 bold").grid(pady=5, padx=65,
                                                                               column=2, row=1, sticky=E, columnspan=3)
        # label Name
        Label(window, text="Name").grid(pady=5,
                                        column=2, row=3, sticky=E)
        # texbox Name
        self.entry_name = Entry(window, width=25)
        self.entry_name.grid(padx=5,column=3, row=3, columnspan=2)

        # Label Subject
        Label(window, text="Subject").grid(pady=5,
                                           column=2, row=4, sticky=E)
        # texbox Subject
        self.entry_subject = Entry(window, width=25)
        self.entry_subject.grid(padx=5,column=3, row=4, columnspan=2)

        # label Message
        Label(window, text="Message").grid(pady=5,
                                           column=2, row=5, sticky=E)
        # texbox Message

        self.entry_message = Text(window, width=33, height=10)
        self.entry_message.grid(padx=5, column=3, row=5, columnspan=2)

        # Label Image
        Label(window, text="Image").grid(
            column=2, row=8, sticky=E)
        # texbox Image
        self.txt_img = StringVar()
        self.entry_image = Entry(window, width=15, textvariable=self.txt_img, state=DISABLED)
        self.entry_image.grid(padx=5, column=3, row=8)

        # Button Upload
        Button(window, width=5, height=1, text="upload", command=self.upload_image).grid(padx=5,
                                                              column=4, row=8)

        # Button Save
        Button(window, width=5, height=1, text="Save", command=self.save_new_template).grid(
            column=1, row=10, columnspan=3, sticky=S)

        self.root.wait_window(window)  # wait until new window closes

    #Button Upload Image Add
    def upload_image(self):
        try:
            self.txt_img.set(filedialog.askopenfilename(filetypes=[("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),]))
            self.img = tkinter.PhotoImage(file=self.txt_img)
        except Exception as e:
            print("upload_image" + str(e))

    #Save New Template
    def save_new_template(self):
        try:
            msge = ''
            # Validate input text
            if self.entry_name.get() != '' and self.entry_subject.get() != '' and self.entry_message.get("1.0", END) != '':
                if not self.controller.validate_message(self.entry_message.get("1.0", END)):
                    self.entry_message.focus_set()
                    msge += "Message does not have a valid format. \n"
                else:
                    if self.controller.add_template_list(self):
                        tkinter.messagebox.showinfo("Information", "Email Template created successfully")
                        self.main_table()
                        # close the window
                        self.entry_name.master.destroy()
                    else:
                        tkinter.messagebox.showerror("Error", "Error creating Email Template")
            else:
                msge += "Name, Subject and Message are required fields."
            if msge != '':
                tkinter.messagebox.showerror("Error", msge)
                self.entry_name.focus_set()
        except Exception as e:
            print("save_new_email " + str(e))

    # Action Delete Button
    def delete_email_template(self, idtemp):
        try:
            confirm = tkinter.messagebox.askyesno(title="Confirmation",
                                                  message="Are you sure that you want to delete this record?")
            if confirm:
                if self.controller.delete_email_template(idtemp):
                    tkinter.messagebox.showinfo("Information", "Email Template deleted successfully!")
                    self.main_table()
                else:
                    tkinter.messagebox.showerror("Error", "Error deleting Email Template!")

        except Exception as e:
            print("delete_email_template " + str(e))

    # Window for edit a template
    def edit_email_template(self, idtemp):
        window = Toplevel(self.root)  # Make new windows in the toplevel of main window
        window.wm_title("Edit Email Template")
        window.geometry("350x500")

        Label(window, text="Edit Email Template", font="Calibri 14 bold").grid(pady=5, padx=65,
                                                                               column=2, row=1, sticky=E,
                                                                               columnspan=3)
       #Retrieve data from the database to edit
        row = self.controller.fecth_one(idtemp)

        # label Name
        Label(window, text="Name").grid(pady=5,
                                        column=2, row=3, sticky=E)
        # texbox Name
        self.txt_name_edit = StringVar()
        self.txt_name_edit.set(row[1])
        self.entry_name_edit = Entry(window, width=25, textvariable=self.txt_name_edit)
        self.entry_name_edit.grid(padx=5, column=3, row=3, columnspan=2)

        # Label Subject
        Label(window, text="Subject").grid(pady=5,
                                           column=2, row=4, sticky=E)
        # texbox Subject
        self.txt_subject_edit = StringVar()
        self.txt_subject_edit.set(row[2])
        self.entry_subject_edit = Entry(window, width=25, textvariable=self.txt_subject_edit)
        self.entry_subject_edit.grid(padx=5, column=3, row=4, columnspan=2)

        # label Message
        Label(window, text="Message").grid(pady=5,
                                           column=2, row=5, sticky=E)
        # texbox Message
        self.entry_message_edit = Text(window, width=33, height=10)
        self.entry_message_edit.insert(0,row[3])
        self.entry_message_edit.grid(padx=5, column=3, row=5, columnspan=2)

        # Label Image
        Label(window, text="Image").grid(
            column=2, row=8, sticky=E)

        #Show image saved in the database
        saved_image = Image.open(io.BytesIO(row[4]))
        saved_image.thumbnail((50,50))
        saved_image = ImageTk.PhotoImage(saved_image)
        Label(window,image=saved_image).grid(
            column=3, row=8, sticky=E)

        # texbox Image
        self.txt_img_edit = StringVar()
        self.entry_image_edit = Entry(window, width=15, textvariable=self.txt_img_edit, state=DISABLED)
        self.entry_image_edit.grid(padx=5, column=3, row=9)

        # Button Upload
        Button(window, width=5, height=1, text="upload", command=self.upload_image_edit).grid(padx=5,
                                                                                         column=4, row=8)

        # Button Save
        Button(window, width=5, height=1, text="Save", command=self.save_new_template).grid(
            column=2, row=10, columnspan=3, sticky=S)

        self.root.wait_window(window)  # wait until new window closes

 #Button Upload Image Edit
    def upload_image_edit(self):
        try:
            self.txt_img_edit.set(filedialog.askopenfilename(filetypes=[("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),]))
            self.img_edit = tkinter.PhotoImage(file=self.txt_img_edit)
        except Exception as e:
            print("upload_image" + str(e))
