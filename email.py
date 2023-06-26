import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'email adress'
email_password = 'code'
email_receivers = ['Email adres', 'Email adress' ]

subject = 'EMAIL TITLE'
body = """
YOUR EMAIL TEXT 

"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    for receiver in email_receivers:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = receiver
        em['Subject'] = subject
        company_name = receiver.split('@')[1].split('.')[0]
        em.set_content(body.format(company_name=company_name))
        
        smtp.send_message(em)
