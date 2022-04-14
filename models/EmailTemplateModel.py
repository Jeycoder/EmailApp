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
    def add(self):
        dbconnect = DBConnection()
        dbconnect.insert("INSERT INTO email_template(Name,Subject,Message, Image) VALUES (%s,%s, %s,%s)",(self.Name, self.Subject, self.message, self.Image))
