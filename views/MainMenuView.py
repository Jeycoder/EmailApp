from tkinter import *
from controllers.EmailTemplateController import EmailTemplateController
from views.report_lists import ReportList


class MainMenu(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Menu Definition
        self.menuBar = Menu(self.parent)
        # add menu to window
        self.parent.config(menu=self.menuBar)

        #Emails submenu
        emails_menu = Menu(self.menuBar)
        emails_menu.add_command(label="Templates", command=self.view_email_templates)
        emails_menu.add_command(label="Lists")
        emails_menu.add_command(label="Send")
        #add Emails menu to the Main Menu
        self.menuBar.add_cascade(label="Emails", menu=emails_menu)

        #Reports submenu
        reports_menu = Menu(self.menuBar)
        reports_menu.add_command(label="Email Lists", command=self.view_reports_list)
        reports_menu.add_command(label="Email Templates")
        reports_menu.add_command(label="Emails Sent")
        # add Reports menu to the Main Menu
        self. menuBar.add_cascade(label="Reports", menu=reports_menu)

    #Call Email Templates View
    def view_reports_list(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        # Call new Window
        win = ReportList(self.parent)
        # Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)


    def view_email_templates(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        #Call new Window
        win = EmailTemplateController(self.parent)
        #Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)




