import jicson
import json
import urllib.request
import smtplib
import inspect
import datetime
import pytz
from email.message import EmailMessage
url = "https://trevor.myschoolapp.com/podium/feed/iCal.aspx?z=[insert calendar id here]"
r = urllib.request.urlretrieve(url)
result = jicson.fromFile(r[0])
for i in result["VCALENDAR"][0]["VEVENT"]:
    if i["SUMMARY"].startswith("Math II A - 1: Homework"):
        d = datetime.datetime.strptime(i["DTEND;VALUE=DATE"], '%Y%m%d') - datetime.timedelta(days=1)
        if int(d.date() == datetime.datetime.now(pytz.timezone('US/Pacific')).date()):
            with open(sys.argv[3]) as recips:
                print("hi")
            break
print("l")