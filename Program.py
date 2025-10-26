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
        if int(i["DTEND;VALUE=DATE"]) == int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d")):
            msg = EmailMessage()
            msg.set_content("REMINDER: Remember to submit your corrections for: {}".format(i["SUMMARY"]))
            msg['Subject'] = "test"
            msg['From'] = "test@domain.tld"
            msg['To'] = ""
            s = smtplib.SMTP('domain.tld')
            s.send_message(msg)
            s.quit()
            break