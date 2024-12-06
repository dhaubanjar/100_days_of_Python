""" code to send email through python"""
from random import Random
import smtplib

random = Random()

def give_quotes():
    with open("quotes.txt", "r") as f:
        all_quotes = f.readlines()
        quotes = random.choice(all_quotes)
        return quotes

""" working with datetime """
import datetime as dt
now = dt.datetime.now()
hour = now.time().hour
if hour == 8:
    my_email = "ryanjustforstocks@gmail.com"
    password = "vqqi xuvi imev oqtp"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()           # TLS - Transport Layer Security, encrypts the email
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rajdhaubanjar007@gmail.com",
            msg=f"Subject:Morning Motivation\n\nQuote of the day: {give_quotes()}",
        )

#---------------------------------------------------------------------------------------------#


