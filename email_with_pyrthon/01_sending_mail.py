import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()

email = getpass.getpass('Enter Your Email : ')
password = getpass.getpass('Enter Your App Password : ')

smtp_object.login(email, password)

from_address = email
to_address = input('Enter Email Address : ')
subject = input('Enter Email Sub : ')
message = input('Enter Message : ')

msg = f'''
    Subject : {subject}
    {message}
'''

smtp_object.sendmail(from_address, to_address, message)

smtp_object.quit()