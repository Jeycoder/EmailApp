from tkinter import *

from tkintertable import TableCanvas, TableModel


class ReportList:
    def __init__(self,controller, root):
        self.controller = controller
        self.root = root
        new_window = Toplevel(root)
        new_window.geometry("750x700")
        new_window.wm_title("Report Email Lists")
        new_window.wait_visibility()

        self.email_frame = Frame(new_window)
        self.email_frame.pack()
        label = Label(new_window, text="Report Email List", font="Calibri 14 bold")
        self.main_table()

        tx_search = StringVar()

        label.place(x=320,y=10)
        Label(new_window,text="Filter: ").place(x=50, y=50)
        Entry(new_window,width=50,textvariable=tx_search).place(x=100,y=50)
        Button(new_window,width=10,text="Search").place(x=450,y=50)
        # wait until new window closes
        root.wait_window(new_window)


 #See Email Lists Table
    def main_table(self):
        # table Creation
        self.model = TableModel()
      #  self.data_table()
        self.table = TableCanvas(self.email_frame, model=self.model, cellbackgr='#e3f698', read_only=True, rowheight=30,
                                 width=600, height=300)
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
                index += 1
            self.model.importDict(data)
        except Exception as e:
            print(str(e))

    def search(self,text):
        try:
            data = dict()
            index = 0
            List_data = self.controller.search(text)
            for row in List_data:
                data[index] = dict()
                data[index]['Id'] = row[0]
                data[index]['Name'] = row[1]
                index += 1
            self.model.importDict(data)
        except Exception as e:
            print("search " + str(e))

