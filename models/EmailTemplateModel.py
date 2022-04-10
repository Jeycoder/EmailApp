from models.db_conn import DBConnection  # Import DB Connection


class EmailTemplate:

    def __init__(self):
        self.dbconnect = None
        self.Id = 0
        self.Subject = ''
        self.Name = ''
        self.email = ''

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        dbconnect = DBConnection()
        return dbconnect.fecth_all("SELECT * FROM email_template")

