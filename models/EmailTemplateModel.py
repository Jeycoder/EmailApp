from models.db_conn import DBConnection  # Import DB Connection


class EmailTemplate:

    def __init__(self,data):
        self.dbconnect = None
        self.Id = 0
        self.Name = ''
        self.Subject = ''
        self.Message = ''
        self.Image = ''

        if data:
            self.Idtem=data[0]
            self.Nametem = data[1]
            self.Subjecttem = data[2]
            self.Messagetem = data[3]
            self.Imagetem = data[4]

    # Retrieve all records in email_template table
    def fecth_all(self) -> object:
        dbconnect = DBConnection()
        return dbconnect.fecth_all("SELECT * FROM email_template")

    #Insert new email Template
    def add(self, view):
        dbconnect = DBConnection()
        email_data = view.txt_name.get(), view.txt_subject.get(), view.txt_message.get(), view.txt_img.get()
        dbconnect.insert("INSERT INTO email_template(Name,Subject,Message, Image) VALUES (%s,%s, %s,%s)",(email_data))

    def SetId(self, id):
        self.Idtem = id

    def SetName(self, name):
        self.Nametem = name

    def SetSubject(self,subject):
        self.Subjecttem=subject

    def SetMessage(self,message):
        self.Messagetem= message

    def SetImage(self, image):
        self.Imagetem = image

    def GetId(self):
        return self.Idtem

    def GetName(self):
        return self.Nametem

    def GetSubject(self):
        return self.Subject

    def GetMessage(self):
        return self.Message
