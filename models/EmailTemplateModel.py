from models.db_conn import DBConnection  # Import DB Connection


class EmailTemplate:

    def __init__(self):
        self.dbconnect = None
        self.Id = 0
        self.Name = ''
        self.Subject = ''
        self.Message = ''
        self.Image = ''

    def __int__(self, id, name, subject,message, image):
        self.Id = id
        self.Name = name
        self.Subject = subject
        self.Message = message
        self.Image = image

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        dbconnect = DBConnection()
        return dbconnect.fecth_all("SELECT * FROM email_template")

    #Insert new email Template
    def add(self, name, subject, message, image):
        try:
            answer = False
            dbc = DBConnection()
            dbc.conn()
            cn = dbc.dbconnect
            cn.autocommit = False
            cn.start_transaction()
            dbc.cursor.execute("INSERT INTO email_template(Name,Subject,Message, Image) VALUES (%s,%s, %s,%s)",(name, subject, message, image))
            cn.commit()
            answer = True
        except Exception as e:
            print("add " + str(e))
            cn.rollback()
            answer = False
        finally:
            dbc.close_cursor()
            return answer

    # delete email template
    def delete(self, id_template):
        try:
            answer = False
            dbc = DBConnection()
            dbc.conn()
            cn = dbc.dbconnect
            dbc.cursor.execute("DELETE FROM email_template WHERE ID =%s", (id_template,))
            cn.commit()
            answer = True
        except Exception as e:
            print("delete " + str(e))
            cn.rollback()
            answer = False
        finally:
            dbc.close_cursor()
        return answer

    #fetch a record from Email Template table
    def fecth_one(self,id_template):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT * FROM "
                                               "email_template WHERE ID = " + str(id_template))
        except Exception as err:
            print("An error has happened at trying get one record from EmailTemplateModel")
            print(err)