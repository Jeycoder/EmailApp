import os
import tkinter.messagebox
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkintertable import TableModel, TableCanvas
from PIL import Image, ImageTk

class EmailListView:
    emailDetails = []  # Email List Details

    def __init__(self, controller: object, root: object) -> object:
        self.model = None
        self.table = None
        self.controller = controller
        self.root = root
        window = Toplevel(root)  # Make new windows in the toplevel of main window
        window.wm_title("Email Lists")
        window.geometry("700x550")

        self.email_frame = Frame(window)
        self.email_frame.pack()
        label = Label(window, text="Email Lists", font="Calibri 14 bold")

        self.main_table()

        label.place(x=320, y=10)
        # Button Add
        btn_add = Button(window, width=5, text="Add", command=self.add_new_email_list_view)
        btn_add.place(x=320, y=420)

        root.wait_window(window)  # wait until new window closes

    #See Email Lists Table
    def main_table(self):
        # table Creation
        self.model = TableModel()
        self.data_table()
        self.table = TableCanvas(self.email_frame, model=self.model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=400, height=300)
        # Add data to the table
        self.table.model = self.model
        self.table.createTableFrame()
        # Show Table
        self.email_frame.place(x=100, y=50)
        self.table.show()

        # Add ACtions buttons
        self.actions_table()

    def data_table(self):
        try:
            data = dict()
            index = 0
            list_lists = self.controller.fetch_all_controller()
            for row in list_lists:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Number of Emails'] = row[2]
                data[index]['Actions'] = ''
                index += 1
            self.model.importDict(data)
        except Exception as e:
            print(str(e))

    def actions_table(self):
        try:
            index = 0
            list_lists = self.controller.fetch_all_controller()
            for row in list_lists:
               #Add button View
                btn_view = Button(self.table, text="V", width=1, command = lambda idl=row[0], namel =row[1] : self.view_email_list_view(idl, namel))
                x1, y1, x2, y2 = self.table.getCellCoords(index, 3)  # Number of columns
                self.table.create_window(((x1 + 1), y1 + 1), anchor=NW, window=btn_view)
                # Add button Delete
                btn_delete = Button(self.table, text="D", width=1, command = lambda idl=row[0] : self.delete_email_list(idl))
                self.table.create_window(((x1 + 50), y1 + 1), anchor=NW, window=btn_delete)
                index += 1
            self.table.update()
        except Exception as e:
            print("actions_table " + str(e))

    #Action Delete Button
    def delete_email_list(self, idlist):
        try:
            confirm = tkinter.messagebox.askyesno(title="Confirmation", message="Are you sure that you want to delete this record?")
            if confirm:
                if self.controller.delete_email_list(idlist):
                    tkinter.messagebox.showinfo("Information", "Email List deleted successfully!")
                    self.main_table()
                else:
                    tkinter.messagebox.showerror("Error", "Error deleting Email List!")

        except Exception as e:
            print("delete_email_list " + str(e))

    # Window for add new list
    def add_new_email_list_view(self):
        try:
            window = Toplevel(self.root)  # Make new windows in the toplevel of main window
            window.wm_title("New Email List ")
            window.geometry("400x500")

            Label(window, text="New Email List", font="Calibri 14 bold").place(x=160, y=20)
            # label Name
            Label(window, text="Name").place(x=20, y=80)
            # texbox Name
            self.txt_name = Entry(window, width=25)
            self.txt_name.place(x=120, y=80)

            frame = Frame(window)
            frame.pack()

            # Setting Columns  for the table
            columns = ("Title", "Name", "Email")

            # Table Details
            self.table_details = Treeview(frame, columns=columns, show='headings')

            # Creating columns
            self.table_details.column("Title", anchor=CENTER, width=60)
            self.table_details.column("Name", anchor=CENTER, width=150)
            self.table_details.column("Email", anchor=CENTER, width=150)

            # setting the heading
            self.table_details.heading("Title", text="Title", anchor=CENTER)
            self.table_details.heading("Name", text="Name", anchor=CENTER)
            self.table_details.heading("Email", text="Email Address", anchor=CENTER)

            # Button add new Email
            add_icon = PhotoImage(file=os.path.abspath('assets/icon_add.png'))
            Button(window, image=add_icon, command=self.add_new_email_view).place(x=300, y=130)

            frame.place(x=20, y=160)
            self.table_details.pack()
            # Button Save
            Button(window, width=5, text="Save", command=self.save_new_email_list).place(x=170, y=450)


            self.root.wait_window(window)  # wait until new window closes
        except Exception as e:
            print("addNewEmailList " + str(e))

    # Windows for add a new Email
    def add_new_email_view(self):
        try:
            window = Toplevel(self.root)  # Make new windows in the toplevel of main window
            window.wm_title("New Email ")
            window.geometry("350x250")

            Label(window, text="New Email", font="Calibri 14 bold").place(x=130, y=20)

            # label Title
            Label(window, text="Title").place(x=20, y=80)
            # texbox Title
            self.combo_title_detail = Combobox(window, width=15, state="readonly")
            self.combo_title_detail["values"] = ("Ms", "Mr", "Mrs")
            self.combo_title_detail.place(x=120, y=80)

            # label Name
            Label(window, text="Name").place(x=20, y=110)
            # texbox Name
            self.entry_name_detail = Entry(window, width=15)
            self.entry_name_detail.place(x=120, y=110)

            # label email
            Label(window, text="Email").place(x=20, y=140)
            # texbox Name
            self.entry_email_detail = Entry(window, width=15)
            self.entry_email_detail.place(x=120, y=140)

            # Button Save
            Button(window, width=5, text="Save", command=self.save_new_email).place(x=130, y=200)


            self.root.wait_window(window)  # wait until new window closes
        except Exception as e:
            print("addNewEmailList " + str(e))

    # Add New Email List Detail
    def save_new_email(self):
        try:
            msge = ''
            # Validate input text
            if self.combo_title_detail.get() != '' and self.entry_name_detail.get() != '' and self.entry_email_detail.get() != '':
                if not self.controller.validate_email(self.entry_email_detail.get()):
                    self.combo_title_detail.focus_set()
                    msge += "Email does not have a valid format. \n"
                else:
                    record = [self.combo_title_detail.get(), self.entry_name_detail.get(),
                              self.entry_email_detail.get()]
                    self.emailDetails.append(record)
                    # Clear the form
                    self.combo_title_detail.delete(0, "end")
                    self.entry_name_detail.delete(0, "end")
                    self.entry_email_detail.delete(0, "end")
                    self.combo_title_detail.focus_set()

                    # add new record to table details
                    self.table_details.insert('', END, values=record)
                    #close the window
                    self.combo_title_detail.master.destroy()
            else:
                msge += "All fields are required"
            if msge != '':
                tkinter.messagebox.showerror("Error", msge)
                self.combo_title_detail.focus_set()
        except Exception as e:
            print("save_new_email " + str(e))

    #Save New Email List and Details
    def save_new_email_list(self):
        try:
            msge = ''
            if self.txt_name.get() == '':
                msge += "Enter a Name for the List. \n"
            if len(self.table_details.get_children()) == 0:
                msge += "Enter at least one email in the list."

            if msge != '':
                tkinter.messagebox.showerror("Email Validation", msge)
                self.txt_name.focus_set()
            else:
                if self.controller.add_email_list(self):
                    tkinter.messagebox.showinfo("Information", "Email List created successfully")
                    self.main_table()
                    # close the window
                    self.txt_name.master.destroy()
                else:
                    tkinter.messagebox.showerror("Error", "Error creating Email List")
        except Exception as e:
            print("save_new_email_list " + str(e))

    #Window for view list
    def view_email_list_view(self, idlist, nameList):
        try:
            window = Toplevel(self.root)  # Make new windows in the toplevel of main window
            window.wm_title("View Email List ")
            window.geometry("400x500")

            Label(window, text="View Email List", font="Calibri 14 bold").place(x=160, y=20)
            # label Name
            Label(window, text="Name").place(x=20, y=80)
            # texbox Name
            txt_variable = StringVar()
            txt_variable.set(nameList)
            self.txt_name = Entry(window, width=25, state = DISABLED, textvariable = txt_variable)
            self.txt_name.place(x=120, y=80)

            frame = Frame(window)
            frame.pack()

            # Setting Columns  for the table
            columns = ("Title", "Name", "Email")

            # Table Details
            self.table_details = Treeview(frame, columns=columns, show='headings')

            # Creating columns
            self.table_details.column("Title", anchor=CENTER, width=60)
            self.table_details.column("Name", anchor=CENTER, width=150)
            self.table_details.column("Email", anchor=CENTER, width=150)

            # setting the heading
            self.table_details.heading("Title", text="Title", anchor=CENTER)
            self.table_details.heading("Name", text="Name", anchor=CENTER)
            self.table_details.heading("Email", text="Email Address", anchor=CENTER)

            #show data in the table details
            list_details = self.controller.fetch_details_controller(idlist)
            for row in list_details:
                self.table_details.insert('', END, values=(row[0], row[1], row[2]))

            frame.place(x=20, y=160)
            self.table_details.pack()
            # Button Save
            Button(window, width=5, text="Close", command=window.destroy).place(x=170, y=450)

            self.root.wait_window(window)  # wait until new window closes
        except Exception as e:
            print("addNewEmailList " + str(e))
