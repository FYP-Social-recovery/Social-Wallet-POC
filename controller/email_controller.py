import smtplib


class EmailController:
    def __init__(self):
        self.email="fypemail98@gmail.com"
        self.password="ocafcqtvmxajdvzr"
    
    def sendEmail(self, receiverEmail, message):
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(self.email, self.password)
        # sending the mail
        s.sendmail(self.email, receiverEmail, message)
        # terminating the session
        s.quit()

#test code--------------------------------------------------
#email_Client=EmailController()
#email_Client.sendEmail("tharindathamaranga98@gmail.com","hi Im tharinda")