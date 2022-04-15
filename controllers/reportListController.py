from views.report_lists import ReportList
from models.reportListModel import reportListModel

class reportListController:
    view = None

    def __init__(self, root):
        self.view = ReportList(self, root)

    def search(self,text):
        report = reportListModel()
        return report.searchList(text)

