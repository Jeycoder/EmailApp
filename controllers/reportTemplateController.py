from views.ReportTemplateView import ReportTemplateView
from models.reportTemplateModel import reportTemplateModel

class ReportTemplateController:
    view = None

    def __init__(self, root):
        self.view = ReportTemplateView(self, root)

    def search(self,text):
        report = reportTemplateModel()
        return report.searchList(text)

    #Retrieve all data in the table
    def fetch_all_controller(self):
        email_list = reportTemplateModel()
        return email_list.fetch_all()