from models.db_conn import DBConnection  # Import DB Connection


class EmailModel:
    Email = ""
    BodyMessage = ""
    Subject = ""

    def __init__(self, email, message, subject):
        self.Email = email
        self.BodyMessage = message
        self.Subject = subject