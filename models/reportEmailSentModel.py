from models.db_conn import DBConnection


class ReportEmailSentModel:

    def __init__(self):
        self.dbConnection = DBConnection()

    def searchList(self, text):
        try:
            db = DBConnection()
            db.conn()
            query = "SELECT r.ReportID, t.Name, l.Name, r.numberEmailSent FROM reports r, email_template t, " \
                    "email_list l WHERE r.numberEmailList = l.IDList and r.numberEmailTemplates = t.id AND(" \
                    "t.Name like '%" + text + "%' or l.Name like '%" + text + "%' or r.numberEmailSent like '%" + text + \
                    "%')"
            db.cursor.execute(query)
            return db.cursor.fetchall()
        except Exception as err:
            print("Search", err)

    def fetch_all(self):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT r.ReportID, t.Name, l.Name, r.numberEmailSent FROM reports r, "
                                               "email_template t, email_list l WHERE r.numberEmailList = l.IDList and"
                                               " r.numberEmailTemplates = t.id")
        except Exception as err:
            print("An error has happened at trying get EmailTemplates from ReportModel")
            print(err)

    def add(self, idList, idTemp, numEmails):
        try:
            answer = False
            dbc = DBConnection()
            dbc.conn()
            cn = dbc.dbconnect
            dbc.cursor.execute("INSERT INTO reports(numberEmailList, numberEmailTemplates, numberEmailSent) VALUES ("
                               "%s, %s, %s)",
                               (idList, idTemp, numEmails))
            cn.commit()
            answer = True
        except Exception as e:
            print("add " + str(e))
            cn.rollback()
            answer = False
        finally:
            dbc.close_cursor()
            return answer
