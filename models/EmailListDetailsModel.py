import asyncio

from models.db_conn import DBConnection


class EmailListDetails:

    def __init__(self, tupleData):
        self.dbConnection = DBConnection()
        self.idemail_list_details = ""
        self.email_list_id = ""
        self.email_title = ""
        self.email_name = ""
        self.email_email = ""

        # Setting all fields from a tuple
        if tupleData:
            self.idemail_list_details = tupleData[0]
            self.email_list_id = tupleData[1]
            self.email_title = tupleData[2]
            self.email_name = tupleData[3]
            self.email_email = tupleData[4]

    # Method to get a List Detail from an ListId
    def GetListDetailFromListId(self, listId):
        try:
            query = "Select * From email_list_details Where email_list_id = '" + str(listId) + "'"
            return self.dbConnection.fecth_all(query)
        except Exception as e:
            print("Has occurred an error trying to get ListDetails from EmailListDetailsModel")
            print(e)
