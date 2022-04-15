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
    def add_email_template(self,view):
        #Attributes from View
        email_temp = EmailTemplate()
        return email_temp.add(view.txt_name.get(),view.txt_subject.get(),view.txt_message.get(),view.txt_image.get(),view.email_temp)

