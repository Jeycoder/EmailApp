from models.db_conn import DBConnection


class reportTemplateModel:

    def __init__(self):
        self.dbConnection = DBConnection()

    def searchList(self, text):
        try:
            db = DBConnection()
            db.conn()
            query = "SELECT * FROM email_template WHERE " \
                    "Name like '%" + text + "%' or Subject like '%" + text + "%' or Message like '%" + text + \
                    "%'"
            db.cursor.execute(query)
            return db.cursor.fetchall()
        except Exception as err:
            print("Search", err)

    def fetch_all(self):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT * FROM email_template")
        except Exception as err:
            print("An error has happened at trying get EmailTemplates from ReportModel")
            print(err)
