from models.db_conn import DBConnection


class reportListModel:

    def __init__(self):
        self.dbConnection = DBConnection()

    def searchList(self, text):
        try:
            db = DBConnection()
            db.conn()
            query = "SELECT * FROM email_list l inner join email_list_details d on l.IDList = d.email_list_id Where " \
                    "name like '%" + text + "%' or email_title like '%" + text + "%' or email_name like '%" + text + \
                    "%' or email_email like '%" + text + "%' "
            db.cursor.execute(query)
            return db.cursor.fetchall()
        except Exception as err:
            print("Search", err)

    def fecth_all(self):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT * FROM email_list l inner join email_list_details d on "
                                               "l.IDList = d.email_list_id")
        except Exception as err:
            print("An error has happened at trying get EmailLists from ReportModel")
            print(err)
