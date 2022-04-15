from models.db_conn import DBConnection


class EmailListModel:

    def __init__(self, tupleData):
        self.dbConnection = DBConnection()
        if tupleData:
            self.IDList = tupleData[0]
            self.Name = tupleData[1]

    def SetId(self, id):
        self.IDList = id

    def SetName(self, name):
        self.Name = name

    def GetId(self):
        return self.IDList

    def GetName(self):
        return self.Name

    # Method to get all EmailList from DB
    def FetchAllEmailList(self):
        try:
            return self.dbConnection.fecth_all("Select * From email_list")
        except:
            print("An error has happened at trying get EmailLists from EmailListModel")
