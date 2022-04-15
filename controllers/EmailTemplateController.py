from models.EmailTemplateModel import EmailTemplate
from views.EmailTemplateView import EmailTemplateView

class EmailTemplateController:
    #Initialize Controller
    def __init__(self, root):
        list = self.fetchAllController()
        self.view = EmailTemplateView(root, list)



    #Select all Email Templates from table
    def fetchAllController(self):
        emailTemp = EmailTemplate()
        return emailTemp.fecth_all()

    #Add New Email template
    def add_email_template(self):
        #Attributes from View
        emailTemp = EmailTemplate()
        emailTemp.Name = self.view.txt_name
        emailTemp.Subject = self.view.txt_subject
        emailTemp.Message = self.view.txt_message
        emailTemp.Image = self.view.txt_img
        emailTemp.Name.get()
        emailTemp.Subject.get()
        emailTemp.Message.get()
        emailTemp.Image.get()

        return emailTemp.add()

