from tkinter import *

from tkintertable import TableCanvas, TableModel


class ReportTemplateView:
    emailDetails = []  # Email List Details
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root
        self.text_to_search = StringVar()
        self.model = TableModel()
        new_window = Toplevel(root)
        new_window.geometry("750x500")
        new_window.wm_title("Report Email Templates")
        new_window.wait_visibility()

        self.email_frame = Frame(new_window)
        self.email_frame.pack()
        label = Label(new_window, text="Report Email Templates", font="Calibri 14 bold")
        self.main_table()

        label.place(x=320, y=10)
        Label(new_window, text="Filter: ").place(x=50, y=50)

        self.txt_search = Entry(new_window, width=50, textvariable=self.text_to_search)
        self.txt_search.place(x=100, y=50)
        Button(new_window, width=10, text="Search",
               command=self.search).place(x=470, y=50)
        # wait until new window closes
        root.wait_window(new_window)

    # See Email Lists Table
    def main_table(self):
        # table Creation
        self.data_table()
        self.table = TableCanvas(self.email_frame, model=self.model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=600, height=250)
        # Add data to the table
        self.table.model = self.model
        self.table.createTableFrame()
        # Show Table
        self.email_frame.place(x=50, y=100)
        self.table.show()

    def data_table(self):
        try:
            data = dict()
            index = 0
            list_lists = self.controller.fetch_all_controller()
            for row in list_lists:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Subject'] = row[2]
                data[index]['Message'] = row[3]
                index += 1
            self.model.importDict(data)
        except Exception as e:
            print(str(e))

    def search(self):
        try:
            data = dict()
            index = 0
            List_data = self.controller.search(self.txt_search.get())
            for row in List_data:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                data[index]['Subject'] = row[2]
                data[index]['Message'] = row[3]
                index += 1
            self.model.deleteRows()
            self.model.importDict(data)
            self.table.redraw()
            self.table.update()
        except Exception as e:
            print("search " + str(e))
