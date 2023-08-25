import datetime as dt
import smtplib
from random import choice
import pandas as pd
import os

my_email = ""
password = ""

birthday = pd.read_csv("birthdays.csv")
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

birthday_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in birthday.iterrows()}


today_date = dt.datetime.now().day
today_month = dt.datetime.now().month
today_tuple = (today_month, today_date)


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    random_file = choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{random_file}") as letter:
        wish = letter.read()
        wish = wish.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'], msg=f"Subject : Happy Birthday !!\n\n{wish}")





