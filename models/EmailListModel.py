from models.db_conn import DBConnection  # Import DB Connection


class EmailListModel:

    def __init__(self, tupleData):
        self.dbConnection = DBConnection()
        self.Id = 0
        self.Name = ''
        self.NumberEmails = 0

        if tupleData:
            self.IDList = tupleData[0]
            self.Name = tupleData[1]

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT IDList,Name,count(d.email_list_id) as numberEmails FROM "
                                               "email_list l left join email_list_details d on l.IDList = "
                                               "d.email_list_id group by IDList")
        except Exception as err:
            print("An error has happened at trying get EmailLists from EmailListModel")
            print(err)

    # Method to get all EmailList from DB
    def FetchAllEmailList(self):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("Select * From email_list")
        except Exception as err:
            print("An error has happened at trying get EmailLists from EmailListModel")
            print(err)

    # Insert new email List
    def add(self, name_list, details_list):
        try:
            answer = False
            dbc = DBConnection()
            dbc.conn()
            cn = dbc.dbconnect
            cn.autocommit = False
            cn.start_transaction()
            dbc.cursor.execute("INSERT INTO email_list(Name) VALUES (%s)", (name_list,))
            last_id = dbc.cursor.lastrowid
            for inx in range(len(details_list)):
                dbc.cursor.execute(
                    "INSERT INTO email_list_details(email_list_id, email_title, email_name, email_email) VALUES ("
                    "%s, %s,%s,%s)",
                    (last_id, details_list[inx][0], details_list[inx][1], details_list[inx][2]))
            cn.commit()
            answer = True
        except Exception as e:
            print("add " + str(e))
            cn.rollback()

            answer = False
        finally:
            dbc.close_cursor()
            return answer

    # delete email list
    def delete(self, id_list):
        try:
            answer = False
            dbc = DBConnection()
            dbc.conn()
            cn = dbc.dbconnect
            cn.autocommit = False
            cn.start_transaction()
            dbc.cursor.execute(
                "DELETE FROM email_list_details WHERE email_list_id=%s",
                (id_list,))
            dbc.cursor.execute("DELETE FROM email_list WHERE IDList =%s", (id_list,))
            cn.commit()
            answer = True
        except Exception as e:
            print("delete " + str(e))
            cn.rollback()
            answer = False
        finally:
            dbc.close_cursor()
            return answer

    def SetId(self, id):
        self.IDList = id

    def SetName(self, name):
        self.Name = name

    def GetId(self):
        return self.IDList

    def GetName(self):
        return self.Name

    # Fecth details from a list
    def fecth_details(self, id_list):
        try:
            self.dbConnection = DBConnection()
            return self.dbConnection.fecth_all("SELECT email_title, email_name, email_email FROM "
                                               "email_list_details WHERE email_list_id = " + str(id_list))
        except Exception as err:
            print("An error has happened at trying get EmailListsDetails from EmailListModel")
            print(err)
