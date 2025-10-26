from crontab import CronTab
with CronTab(user='user') as cron:
    jobs = cron.find_command("python3 MathCorrections/Program5.py")
    for job in jobs:
        print(job)