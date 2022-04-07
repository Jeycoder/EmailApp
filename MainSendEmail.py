from controllers.SendEmail import SendEmail

senderEmail = "students.lambton.csam@gmail.com"
senderPassword = "PythonProject**"

# Creating the instance to call main class
sendEmail = SendEmail("This is the email subject")

# Calling the method to get data to send
emailsToSend = sendEmail.SetDataToSend()

# Calling method to configure server
sendEmail.ConfigureServerAndSendEmail(senderEmail, senderPassword, emailsToSend)

