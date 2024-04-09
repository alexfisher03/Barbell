import smtplib
from decouple import config

SENDGRID_API_KEY = ''
FROM_EMAIL = ''
TO_EMAIL = ''

subject = "Hello, World!"
body = "This is a test email sent from a Python script!"

email_text = f"""\
From: {FROM_EMAIL}
To: {TO_EMAIL}
Subject: {subject}

{body}
""" 


    
