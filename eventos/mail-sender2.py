import os
from django.conf import settings
import smtplib, ssl
from django.db import models
import re
from requests_html import HTMLSession

email_user = 'goncalomatos007@gmail.com'
email_password = 'SUpertramp007'



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_user, email_password)
        

        subject = 'xpto'
        body = 'xpto'

        msg = f'Subject: {subject} \n\n {body}'

        smtp.sendmail(email_user, 'goncalomatos007@gmail.com', msg)
    
url = "https://www.randomlists.com/email-addresses"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
session = HTMLSession()

r = session.get(url)
r.html.render()

for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(re_match.group())