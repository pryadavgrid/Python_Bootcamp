import imaplib
import getpass
import email


my_imap_obj = imaplib.IMAP4_SSL('imap.gamil.com')

my_email = getpass.getpass('Enter Email : ')
password = getpass.getpass('Enter Password : ')

my_imap_obj.login(my_email, password)

# my_imap_obj.list()

my_imap_obj.select('inbox')

# typ, data = my_imap_obj.search(None, 'ALL')
typ, data = my_imap_obj.search(None, 'UNSEEN')
# typ, data = my_imap_obj.search(None, 'FROM username@gamil.com')

# print(typ, data)
msg_id = data[0]

result, email_data = my_imap_obj.fetch(msg_id)

# print(email_data)

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_msg = email.message_from_string(raw_email_string)
# print(email_msg) # iterator

for part in email_msg.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body) 