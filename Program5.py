import jicson
import urllib.request
import smtplib
import datetime
import pytz
import ssl
import sys
import imaplib
from crontab import CronTab
from dotenv import load_dotenv
import os
load_dotenv()
def sendText(assignment, hrs, recips):
    cron = CronTab(user='user')
    sender = "user@gmail.com"
    pswd = os.getenv("password")
    con = imaplib.IMAP4_SSL('imap.gmail.com')
    con.login(sender, pswd)
    con.select('Inbox')
    context = ssl.create_default_context()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls(context=context)
    s.login(sender, pswd)
    msg = "\nREMINDER: Remember to submit your corrections for: {}. Send 'submitted' to stop receiving these.".format(assignment)
    recips2 = []
    for l in recips:
        if hrs == 0:
            l = l.partition('#')[0]
            l = l.rstrip()
        if (str(con.search(None, "(BODY 'submitted' FROM "+l.split("@")[0]+" UNSEEN)")[1]).split("'")[1].split(" ") == ['']):
            s.sendmail(sender, l, msg)
            recips2.append(l)
    jobs = cron.find_command("python3 MathCorrections/Program5.py")
    for job in jobs:
        if hrs < 4:
            job.set_command("python3 MathCorrections/Program5.py '{}' '{}' '{}'".format(assignment, hrs+1, recips2))
            if 22+hrs > 23:
                job.setall("0 " + str(hrs-2) + " * * *")
            else:
                job.setall("0 " + str(22+hrs) + " * * *")
        elif hrs == 4:
            job.set_command("python3 MathCorrections/Program5.py '{}' '{}' '{}'".format("OOPS", 0, "MathCorrections/Recipientes.txt"))
            job.setall("0 " + str(21) + " * * *")
        cron.write()
    s.quit()
hours = int(sys.argv[2])
if hours == 0:
    url = "https://trevor.myschoolapp.com/podium/feed/iCal.aspx?z=[insert calendar id here]"
    r = urllib.request.urlretrieve(url)
    result = jicson.fromFile(r[0])
    for i in result["VCALENDAR"][0]["VEVENT"]:
        if i["SUMMARY"].startswith("Math II A - 1: Homework"):
            d = datetime.datetime.strptime(i["DTEND;VALUE=DATE"], '%Y%m%d') - datetime.timedelta(days=1)
            if d.date() == datetime.datetime.now(pytz.timezone('US/Pacific')).date():
                print("hi")
                with open(sys.argv[3]) as recips:
                    sendText(i["SUMMARY"], 0, recips)
                break
elif hours < 5:
    sendText(sys.argv[1], hours, sys.argv[3].replace("[", "").replace("]", "").split(", "))