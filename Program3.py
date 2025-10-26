import jicson
import urllib.request
import smtplib
import datetime
import pytz
import ssl
url = "https://trevor.myschoolapp.com/podium/feed/iCal.aspx?z=[insert calendar id here]"
r = urllib.request.urlretrieve(url)
result = jicson.fromFile(r[0])
for i in result["VCALENDAR"][0]["VEVENT"]:
    if i["SUMMARY"].startswith("Math II A - 1: Homework"):
        if int(i["DTEND;VALUE=DATE"])-1 == int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d")):
            sender = "user@trevor.org"
            s = smtplib.SMTP('localhost')
            msg = "\nREMINDER: Remember to submit your corrections for: {}".format(i["SUMMARY"])
            with open("MathCorrections/Recipientes.txt") as recips:
                for l in recips:
                    l = l.partition('#')[0]
                    l = l.rstrip()
                    s.sendmail("number@provider.tld", l, msg)
            s.quit()
            break