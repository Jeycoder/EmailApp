import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models.Email import Email
from models.UserEmailList import UserEmailList

class SendEmail:
    _subject = ""

    def __init__(self, subject):
        self._subject = subject

    def SetDataToSend(self):

        # Setting values of data to replace
        usernameReplace = "{Username}"
        titleReplace = "{Title}"
        emailsToSend = []

        # This is data to test. It should be replaced by data in DB
        userEmail = UserEmailList(1, "Mr", "Deiby Montoya", "deiby.sk@hotmail.com")
        userEmail2 = UserEmailList(2, "Mrs", "Leandro Lopez", "dmontoya.sk@gmail.com")
        userEmail3 = UserEmailList(3, "Ms", "Jessica Alvarez", "jessica.alvarezmir@gmail.com")
        userEmailList = [userEmail, userEmail2, userEmail3]

        # Opening the file. It should be replaced by data in DB.
        file = open("template1.txt", "r")
        data = file.read()
        file.close()

        # Iterating the content of each user to replace values in the email body
        for user in userEmailList:
            message = data.replace(titleReplace, user.Title).replace(usernameReplace, user.Name)
            email = Email(user.Email, message, self._subject)
            emailsToSend.append(email)

        return emailsToSend


    def ConfigureServerAndSendEmail(self, senderEmail, senderPassword, emailsToSend):

        # Creating the SMTP session to send email
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(senderEmail, senderPassword)

        # Iterating each user to send email to any of those
        for bodyMessage in emailsToSend:

            # Setting up the MIME
            messageToSend = MIMEMultipart()
            messageToSend["From"] = senderEmail

            session.login(senderEmail, senderPassword)
            messageToSend["To"] = bodyMessage.Email
            messageToSend["Subject"] = bodyMessage.Subject
            messageToSend.del_param("attach")
            messageToSend.attach(MIMEText(bodyMessage.BodyMessage, "plain"))

            plainText = messageToSend.as_string()
            session.sendmail(senderEmail, bodyMessage.Email, plainText)
            print("Email sent")

        # Closing session
        session.quit()


