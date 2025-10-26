import smtplib
import ssl
import sys
number = sys.argv[1]
s = smtplib.SMTP('localhost')
context = ssl.create_default_context()
sender = "user@trevor.org"
with open("gateways.txt") as recips:
    for l in recips:
        s.sendmail(sender, number + l, l)