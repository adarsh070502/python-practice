import os
import smtplib

my_email = "adarsheluri123@gmail.com"
password = os.environ.get("EMAIL_PASSWORD")

with smtplib.SMTP("smtp.gmail.com",587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="adarsheluri143@gmail.com",
                        msg="Subject: Hello adarsh\n\n"
                            "how are you")
    connection.close()