import datetime as dt
import smtplib
from random import choice

my_email = ""
password = "" #App password from google account

with open("quotes.txt") as text:
    quote = choice(text.readlines())

current_weekday = dt.datetime.now().weekday()

if current_weekday == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Motivational Quote of the Day\n\n{quote}")


