
import smtplib, ssl
from django.db import models


import sys
import os
import django

sys.path.append('C:/Users/gonca/Arabesco_new2')
os.environ['DJANGO_SETTINGS_MODULE'] = 'arabesco.settings'
django.setup()

from django.contrib.auth.models import User


email_user = 'goncalomatos007@gmail.com'
email_password = 'SUpertramp007'

recievers = []
for user in User.objects.all():
    recievers.append(user.email)
    print(recievers)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_user, email_password)
        

        subject = 'xpto'
        body = 'xpto'

        msg = f'Subject: {subject} \n\n {body}'

        smtp.sendmail(email_user, recievers , msg)