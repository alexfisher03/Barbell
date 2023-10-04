"""
import smtplib

# Replace these variables with your details
SENDGRID_API_KEY = ''
FROM_EMAIL = 'barbellauth@socialbarbell.com'
TO_EMAIL = 'gitbodied@gmail.com'

subject = "Hello, World!"
body = "This is a test email sent from a Python script!"

email_text = f""(")<-fix****\
From: {FROM_EMAIL}
To: {TO_EMAIL}
Subject: {subject}

{body}
""(")<-fix**** 

# Send the email
try:
    server = smtplib.SMTP('smtp.sendgrid.net', 587)
    server.starttls()
    server.login('apikey', SENDGRID_API_KEY)
    server.sendmail(FROM_EMAIL, TO_EMAIL, email_text)
    server.quit()

    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
    
    """
