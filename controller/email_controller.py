import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailController:
    def __init__(self):
        self.email="fypemail98@gmail.com"
        self.password="ocafcqtvmxajdvzr"
    
    def sendEmail(self, receiverEmail, OTP):
        # Create a multipart message object
        message = MIMEMultipart()
        # Set the message body
        message.attach(MIMEText(str(OTP)+' is your One-Time Password (OTP) for Social Wallet.\n\nFor security purposes, kindly do not share this OTP with anyone.'))
        # Set the subject
        message['Subject'] = 'Social Wallet One Time Password (OTP)'
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(self.email, self.password)
        # sending the mail
        s.sendmail(self.email, receiverEmail, message.as_string())
        # terminating the session
        s.quit()

#test code--------------------------------------------------
# email_Client=EmailController()
# email_Client.sendEmail("tharindathamaranga98@gmail.com","2585")