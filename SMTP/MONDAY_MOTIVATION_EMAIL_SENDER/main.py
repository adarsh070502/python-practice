import os
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:

    with open(r"quotes.txt") as data:
        quotes_list = data.readlines()

    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        my_email = "adarsheluri123@gmail.com"
        password = os.environ.get("EMAIL_PASSWORD")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="adarsheluri143@gmail.com",
                            msg=f"Subject: MONDAY MOTIVATION\n\n{quote}")
