import mysql.connector #connect to databse

class DBConnection:
    def __init__(self) -> object:
       self.cursor = None
       self.dbconnect = None
       self.rows = None
       self.host = "localhost"
       self.user = "jessica"
       self.password = "Valledupar123"
       self.db = "python"
       self.auth = "mysql_native_password"

      #Connect to the database
    def conn(self):
        self.dbconnect = mysql.connector.connect(host=self.host,
                                                 user=self.user,
                                                 password=self.password,
                                                 database=self.db,
                                                 auth_plugin=self.auth)

        self.cursor = self.dbconnect.cursor()
        self.dbconnect.autocommit = False

    #Fecth all Rows
    def fecth_all(self, query):
        self.conn() #connect to DB
        self.cursor.execute(query)#Execute Qyuery
        self.rows = self.cursor.fetchall() #Retrieve all Records
        self.close_cursor()
        return self.rows

    def insert(self, query, args):
        self.conn()  # connect to DB
        if args != '':
            self.cursor.execute(query,args)  # Execute Qyuery
            self.dbconnect.commit()
            self.close_cursor()

    #Close Cursor
    def close_cursor(self):
        self.cursor.close()


