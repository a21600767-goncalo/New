import os
import django
import smtplib, ssl
from django.db import models
from eventos.models import Evento2


email_user = 'goncalomatos007@gmail.com'
email_password = 'SUpertramp007'

'''
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_user, email_password)
        

        subject = 'xpto'
        body = 'xpto'

        msg = f'Subject: {subject} \n\n {body}'

        smtp.sendmail(email_user, 'goncalomatos007@gmail.com', msg)
  '''  

recievers = []
for user in User.objects.all():
    recievers.append(user.email)
    print(recievers)