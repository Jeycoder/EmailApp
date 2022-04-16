from views.ReportEmailSentView import ReportEmailSentView
from models.reportEmailSentModel import ReportEmailSentModel

class ReportEmailSentController:
    view = None

    def __init__(self, root):
        self.view = ReportEmailSentView(self, root)

    def search(self,text):
        report = ReportEmailSentModel()
        return report.searchList(text)

    #Retrieve all data in the table
    def fetch_all_controller(self):
        sent_list = ReportEmailSentModel()
        return sent_list.fetch_all()