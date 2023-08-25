import smtplib

my_email = ""
password = ""

#connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email, to_addrs="", msg="Subject:Hello\n\nThis is testing mail, sent from python.")
#connection.close()