import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import asyncio

import numpy
import numpy as np

from models.EmailListDetailsModel import EmailListDetails
from models.EmailListModel import EmailListModel
from models.EmailModel import EmailModel
from models.EmailTemplateModel import EmailTemplate

class SendEmailController:
    _subject = ""
    npEmailList = numpy.array([], dtype=EmailListModel)
    npUsersList = numpy.array([], dtype=EmailListDetails)

    def __init__(self, root):
        self.listEmailTemplate = None
        self.listEmailList = None
        self.root = root

    def GetDataList(self):
        self.listEmailList = self.GetAllEmailList()
        self.listEmailTemplate = self.GetAllTemplatelList()

    def SetDataToSend(self, emailListId, templateList):

        try:
            # Creating the instance of class
            emailListDetails = EmailListDetails({})
            emailsToSend = []

            usersList = emailListDetails.GetListDetailFromListId(emailListId)

            # Awaiting just 1/2 second to avoid doing all the chain of functions in an async way
            time.sleep(0.5)

            if len(usersList) > 0:
                # Maping all data into variable with class type EmailListDetails
                for userData in usersList:
                    userDetail = EmailListDetails(userData)
                    self.npUsersList = numpy.append(self.npUsersList, [userDetail])

                    # Setting values of data to replace
                    usernameReplace = "{Username}"
                    titleReplace = "{Title}"


                    # Setting the data to be replaced
                    emailBody = templateList[3]
                    self._subject = templateList[2]

                    # Iterating the content of each user to replace values in the email body
                    for user in self.npUsersList:
                        message = emailBody.replace(titleReplace, user.email_title).replace(usernameReplace, user.email_name)
                        email = EmailModel(user.email_email, message, self._subject)
                        emailsToSend.append(email)
            else:
                print("There's no data in table: email_list_details")

            return emailsToSend
        except Exception as err:
            print("Error at trying map the data, SendEmailController")
            print(err)

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
            print('Email to ' + bodyMessage.Email + ' has been successfully sent!')

        # Closing session
        session.quit()

    def GetAllEmailList(self):
        try:
            emailModel = EmailListModel(self.npEmailList)
            list = emailModel.FetchAllEmailList()

            # Validating if there's at least one row
            if len(list) > 0:
                # Adding each row to global row with class type: EmailListModel
                for index in range(len(list)):
                    listEmail = EmailListModel(list[index])
                    self.npEmailList = numpy.append(self.npEmailList, [listEmail])
            else:
                print("There's no rows in DB for Email_List")

            return self.npEmailList
        except:
            print("An error has occurred in SendEmailController => GetEmailList")

    def GetAllTemplatelList(self):
        templateModel = EmailTemplate()
        return templateModel.fecth_all()
