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

