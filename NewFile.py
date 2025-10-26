import imaplib, email
sender = "user@gmail.com"
pswd = "password"
con = imaplib.IMAP4_SSL('imap.gmail.com')
con.login(sender, pswd)
con.select('Inbox')
add = str(con.search(None, '(BODY "add me to the math program")')[1]).split("'")[1].split(" ")
for i in add:
    f = con.fetch(i, "(RFC822)")[1][0][1]
    msg = email.message_from_bytes(f)
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            print(str(con.fetch(i, "(BODY[HEADER.FIELDS (FROM)])")[1][0][1]).split("<")[1].split(">")[0] + " #"+str(part).split("\n")[2].split(":")[0])
