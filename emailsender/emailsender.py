from email.message import EmailMessage
from passw import password
import ssl
import smtplib


email_sender = "" # your email
email_password = password # your password, from generate app password at google security

email_receiver = "" # random email from web temp email

subject = "Fact about Abimael"
body = """
Hi Abimael, i know you are GAY....just be yourself....peace
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


