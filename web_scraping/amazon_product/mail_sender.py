import os
import smtplib

class Mail:
    def __init__(self):
        pass
    def send_mail(self,message):
        print("sending mail")
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            my_email = "adarsheluri123@gmail.com"
            password = os.environ.get("EMAIL_PASSWORD")
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="adarsheluri143@gmail.com",
                                msg=message)