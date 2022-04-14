from models.db_conn import DBConnection  # Import DB Connection


class EmailTemplate:

    def __init__(self):
        self.dbconnect = None
        self.Id = 0
        self.Subject = ''
        self.Name = ''
        self.Image = ''

    def __int__(self, id, subject, name, image):
        self.Id = id
        self.Subject = subject
        self.Name = name
        self.Image = image

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        dbconnect = DBConnection()
        return dbconnect.fecth_all("SELECT * FROM email_template")

    #Insert new email Template
    def add(self):
        dbconnect = DBConnection()
        dbconnect.insert("INSERT INTO email_template(Name,Subject,Message, Image) VALUES (%s,%s, %s)",(self.Name, self.Subject, self.Email, self.Image))
