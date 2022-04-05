class EmailTemplate:
    Id = int()
    Subject = str()
    Name = str()
    Message = str()

    def __init__(self, id, subject, name, email):
        self.Id = id
        self.Subject = subject
        self.Name = name
        self.email = email


