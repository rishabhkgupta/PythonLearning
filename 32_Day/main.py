import pandas as pd
import datetime as dt
import smtplib
import random


sender_email = ""
sender_password = ""
letter_list = [r"32_Day\letter_templates\letter_1.txt", r"32_Day\letter_templates\letter_2.txt", r"32_Day\letter_templates\letter_3.txt"]


now = dt.datetime.now()
month = now.month
date = now.day

data = pd.read_csv(r"32_Day\birthdays.csv")

for index, row in data.iterrows():
    if row.month == month and row.day == date:
        with open(random.choice(letter_list)) as file:
            letter = file.read()
            name = row["name"]
            final_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{final_letter}"
            )
