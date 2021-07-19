
import os
import smtplib
from smtplib import SMTP
import schedule
import time
import datetime
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

email_user = 'goncalomatos007@gmail.com'
email_password = 'SUpertramp007'

def mailsender():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_user, email_password)
        now = datetime.datetime.now()

        subject = 'xpto'
        body = 'xpto'

        msg = f'Subject: {subject} \n\n {body}'


        #smtp.sendmail(email_user, 'goncalomatos007@gmail.com', msg)
        html_content = render_to_string('facebook-html-copy.html')
        
        email = EmailMultiAlternatives(


        )
        email.attach_alternative(html_content, "text/html")
        email.send()

    #if(Evento2.data_evento < now + timedelta(days=10)):    
        schedule.every(20).seconds.do(mailsender)

while True:
    mailsender()

