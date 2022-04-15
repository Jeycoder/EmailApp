import asyncio
from tkinter import *
from tkinter.ttk import Combobox

from controllers.SendEmailController import SendEmailController


class MainSendEmailView:


    def __init__(self, root, listUserEmails, listTemplates):
        super().__init__()

        self.listUserEmails = listUserEmails
        self.listTemplates = listTemplates
        self.root = root
        self.senderEmail = "students.lambton.csam@gmail.com"
        self.senderPassword = "PythonProject**"

        # Creating new instance
        widget = Tk()
        widget.wm_title("Sending emails")
        widget.geometry("600x400")

        # Title label
        label = Label(widget, text="Send Emails", font="Calibri 20 bold")
        label.grid(row=0, column=5)

        # Email list
        label = Label(widget, text="Email List", font="Calibri 14", width=20, height=5, pady=10)
        label.grid(row=3, column=3)

        # Select Email list
        # Next line: Getting values by Name property.
        dataByName = list(map(lambda x: x.Name, self.listUserEmails))
        self.selectEmailList = Combobox(widget, state='readonly', values=dataByName, width=20, height=7)
        self.selectEmailList.current(0)  # Setting the first value as default
        self.selectEmailList.grid(row=3, column=6)

        # Template list
        label = Label(widget, text="Email Template", font="Calibri 14", width=20, height=7)
        label.grid(row=4, column=3)

        # Select Email list
        dataByName = list(map(lambda x: x[1], self.listTemplates))
        self.selectEmailTemplate = Combobox(widget, state='readonly', values=dataByName, width=20, height=7)
        self.selectEmailTemplate.current(0)  # Setting the first value as default
        self.selectEmailTemplate.grid(row=4, column=6)

        # Button Send
        btn_add = Button(widget, width=10, height=2, text="Send", command=self.SendEmails, borderwidth=0)
        btn_add.grid(row=6, column=5)

        root.wait_window(widget)

    # Method to trigger send emails getting the id for each value
    def SendEmails(self):
        try:
            # Getting the ID selected
            emailListId = list(filter(lambda em: em.Name == self.selectEmailList.get(), self.listUserEmails))[0].IDList
            templateList = list(filter(lambda em: em[1] == self.selectEmailTemplate.get(), self.listTemplates))[0]
            sendEmailController = SendEmailController(self.root)

            # Calling to other class to Set data to send emails
            emailsToSend = sendEmailController.SetDataToSend(emailListId, templateList)

            sendEmailController.ConfigureServerAndSendEmail(self.senderEmail, self.senderPassword, emailsToSend)

        except Exception as err:
            print("Error in Action button trying to get Id from Value")
            print(err)


