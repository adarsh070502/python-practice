import os
import smtplib
import random
import pandas
import datetime as dt


now = dt.datetime.now()
date = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
birth_data = data.to_dict(orient="records")

for i in range(len(birth_data)):
    person_date = birth_data[i]["date"]
    person_month = birth_data[i]["month"]
    person_name = birth_data[i]["name"]

    if date == person_date and person_month == month:
        rf = random.randint(1,3)
        with open(f"letter_{rf}.txt") as letter_data:
            letter = letter_data.read()
            letter1 = letter.replace("[NAME]", person_name)

        with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection:
            my_email = "adarsheluri123@gmail.com"
            password = os.environ.get("EMAIL_PASSWORD")
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="adarsheluri143@gmail.com",
                                msg=f"Subject: HAPPY BIRTHDAY!!\n\n{letter1}")





