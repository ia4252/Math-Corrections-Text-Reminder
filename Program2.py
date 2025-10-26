import jicson
import json
import urllib.request
import smtplib
import inspect
import datetime
import pytz
import ssl
url = "https://trevor.myschoolapp.com/podium/feed/iCal.aspx?z=[insert calendar id here]"
r = urllib.request.urlretrieve(url)
result = jicson.fromFile(r[0])

for i in result["VCALENDAR"][0]["VEVENT"]:
    if i["SUMMARY"].startswith("Math II A - 1: Homework"):
        if int(i["DTEND;VALUE=DATE"])-1 == int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d")):
            context = ssl.create_default_context()
            sender = "user@gmail.com"
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls(context=context)
            s.login(sender, "password")
            msg = "\nREMINDER: Remember to submit your corrections for: {}".format(i["SUMMARY"])
            msg = ""
            recipientes = [
                            "number@provider.tld", #name
                            "number@provider.tld", #name
                            "number@provider.tld", #name
            ]
            for r in recipientes:
                s.sendmail(sender, r, msg)
            s.quit()
            break