from models.db_conn import DBConnection  # Import DB Connection


class EmailList:

    def __init__(self):
        self.dbconnect = None
        self.Id = 0
        self.Name = ''
        self.NumberEmails = 0

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        dbconnect = DBConnection()
        return dbconnect.fecth_all("SELECT IDList,Name,count(d.email_list_id) as numberEmails FROM email_list l left join email_list_details d on l.IDList = d.email_list_id group by IDList")

    #Insert new email List
    def add(self,name_list, details_list):
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
                    (last_id,details_list[inx][0], details_list[inx][1], details_list[inx][2]))
            cn.commit()
            answer = True
        except Exception as e:
            print("add " + str(e))
            cn.rollback()

            answer = False
        finally:
            dbc.close_cursor()
            return answer