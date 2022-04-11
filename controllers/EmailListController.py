from models.EmailTemplateModel import EmailTemplate
from views.EmailListView import EmailListsView

class EmailListController:
    #Initialize Controller
    def __init__(self, root):
        list = self.fetchAllController()
        self.view = EmailListsView(root, list)



    #Select all Email Templates from table
    def fetchAllController(self):
        emailTemp = EmailTemplate()
        return emailTemp.fecth_all()

    #Add New Email template
    def add_emai_template(self):
        #Attributes from View

        emailTemp = EmailTemplate()
