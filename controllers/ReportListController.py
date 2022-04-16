from views.ReportListView import ReportListView
from models.reportListModel import reportListModel

class ReportListController:
    view = None

    def __init__(self, root):
        self.view = ReportListView(self, root)

    def search(self,text):
        report = reportListModel()
        return report.searchList(text)

    #Retrieve all data in the table
    def fetch_all_controller(self):
        email_list = reportListModel()
        return email_list.fecth_all()