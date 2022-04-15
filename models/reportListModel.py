from models.db_conn import DBConnection

class reportListModel:

    def __init__(self,text):
        self.dbConnection = DBConnection()

    def searchList(self,text):
        try:
            db=DBConnection()
            db.conn()
            db.cursor.execute("SELECT * FROM email_list Where name=" + text)
            return db.cursor.fetchall()
        except Exception as err:
            print("Search",err)


