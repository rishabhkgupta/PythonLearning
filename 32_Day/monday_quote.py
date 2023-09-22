import smtplib
import datetime as dt
import random


sender_email = "birthdaywishesbyrishabh@gmail.com"
sender_password = "wikadsdstqoovdov"
reciver_email= "jahnavi.gupta2000@gmail.com"
quote_of_the_day = ""
quort_by = ""

# ----------------- GET QUOTE -----------------------
quote_list = []

with open(r"32_Day\quotes.txt") as quotes:
    quote_list = quotes.readlines()

original_string = random.choice(quote_list)
parts = original_string.split(" - ")
print(parts)
# Check if there are exactly two parts
if len(parts) == 2:
    quote_of_the_day, quort_by = parts
    print(quote_of_the_day)
    print(quort_by)
else:
    print("Invalid input format: Expected a single hyphen in the string.")


# ------------------- SEND THE QUOTE-----------------

now = dt.datetime.now()
day = now.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    if day == 0:
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=reciver_email,
            msg=f"Subject:Quote of the day\n\n{quote_of_the_day}\n\n{quort_by}"
        )