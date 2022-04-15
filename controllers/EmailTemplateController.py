from tkinter import END

from models.EmailTemplateModel import EmailTemplate
from views.EmailTemplateView import EmailTemplateView

class EmailTemplateController:
    view = None

    #Initialize Controller
    def __init__(self, root):
        self.view = EmailTemplateView(self, root)

    #Select all Email Templates from table
    def fetchAllController(self):
        email_temp = EmailTemplate()
        return email_temp.fecth_all()

    #Add New Email template
    def add_template_list(self,view):
        #Attributes from View
        email_temp = EmailTemplate()
        return email_temp.add(view.entry_name.get(),view.entry_subject.get(),view.entry_message.get("1.0", END),view.img)

    #Validate if a message has a {Title} and an {Username}
    def validate_message(self, text):
        try:
            if not ("{Title}" in text and "{Username}" in text):
                return False
            else:
                return True
        except Exception as e:
            print("validate_email " + str(e))
            return False

    # Delete an Email Template
    def delete_email_template(self, idTemplate):
        email_temp = EmailTemplate()
        return email_temp.delete(idTemplate)

    #fecth one record
    def fecth_one(self, idTemp):
        email_temp = EmailTemplate()
        return email_temp.fecth_one(idTemp)