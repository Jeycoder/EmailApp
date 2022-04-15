import re
from models.EmailListModel import EmailListModel
from views.EmailListView import EmailListView

class EmailListController:
    view = None
    #Initialize Controller

    def __init__(self, root):
        self.view = EmailListView(self, root)

    #validate an Email
    def validate_email(self, text):
        try:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.match(pattern,text):
                return False
            else:
                return True
        except Exception as e:
            print("validate_email " + str(e))
            return False

    #Select all Email Lists from table
    def fetch_all_controller(self):
        email_list = EmailListModel({})
        return email_list.fecth_all()

   # Add New Email List
    def add_email_list(self,view):
        # Attributes from View
        email_list = EmailListModel({})
        return email_list.add(view.txt_name.get(), view.emailDetails)
