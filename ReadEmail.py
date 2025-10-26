# Importing libraries
import imaplib, email
 
user = 'user@gmail.com'
password = 'password'
imap_url = 'imap.gmail.com'
 
# Function to get email content part i.e its body part
# this is done to make SSL connection with GMAILs
con = imaplib.IMAP4_SSL('imap.gmail.com') 
 
# logging the user in
con.login(user, password) 
 
# calling function to check for email under this label
con.select('Inbox')
f = "number@provider.tld"
if (str(con.search(None, "(BODY 'stop' FROM "+f.split("@")[1]+" UNSEEN)")[1]).split("'")[1].split(" ") == ['']):
    print("hi")# if (str(con.search(None, "(BODY 'stop' FROM "+f+" UNREAD)")[1]).split("'")[1].split(" ") == ['']):
#             print("6")