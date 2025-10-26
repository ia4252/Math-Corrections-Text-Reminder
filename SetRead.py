import imaplib
from dotenv import load_dotenv
import os
load_dotenv()
sender = "user@gmail.com"
pswd = os.getenv("pswd")
con = imaplib.IMAP4_SSL('imap.gmail.com')
con.login(sender, pswd)
con.select('Inbox')
unr = str(con.search(None, "(BODY 'submitted' UNSEEN)")[1][0]).replace("b'", "").replace("'", "")
for i in unr.split(" "):
    con.store(i, "+FLAGS", "\\Seen")