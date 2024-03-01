import smtplib
from decouple import config

# Replace these variables with your details
SENDGRID_API_KEY = ''
FROM_EMAIL = 'barbellauth@socialbarbell.com'
TO_EMAIL = 'gitbodied@gmail.com'

subject = "Hello, World!"
body = "This is a test email sent from a Python script!"

email_text = f"""\
From: {FROM_EMAIL}
To: {TO_EMAIL}
Subject: {subject}

{body}
""" 


    
