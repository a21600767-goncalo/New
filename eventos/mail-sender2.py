
import smtplib, ssl
from django.db import models
import sys
import os
import django

sys.path.append('C:/Users/gonca/Arabesco_new2')
os.environ['DJANGO_SETTINGS_MODULE'] = 'arabesco.settings'
django.setup()

from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
import os
import re
import requests
import facebook as fb
from datetime import datetime, timedelta, time
import urllib.request
from urllib.request import urlopen
from email.message import EmailMessage
import imghdr
from PIL import Image
import shutil
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.template import loader

def mailsender():

    email_user = 'goncalomatos007@gmail.com'
    email_password = 'SUpertramp007'

    cloudinary.config( 
        cloud_name = "da7qp20ja", 
        api_key = "835922641349356", 
        api_secret = "qt3MG0N2omjL_7kS_khMi7k5_1c"
        )

    tag ='evento-canvas'

    time_today = datetime.now()

    time_x = time_today + timedelta(days=0) 

    time2 = time_x.strftime("%Y-%m-%d")

    result = cloudinary.Search()\
    .expression(tag)\
    .execute()

        
    cloud = 'http://res.cloudinary.com/da7qp20ja/image/upload/'
    
    cloud_tag = cloud + tag
    print(result)
    print(requests.__version__)

    z= cloudinary.api.resources_by_tag("url")
        
        
    j = json.dumps(result)
    w = ''.join(j)
    stripped_string = w.replace('"', '')
    q = list(j.split(' '))
        
    urls =[[a] for a in q if cloud in a]
    urls2 = [''.join(ele) for ele in urls]
    urls3 = ''.join(urls2)
    urls4 = urls3.replace('"', '')
    urls_list = list(urls4.split(","))

    


    print(urls)

    url=""
    link =""
    for url in urls_list:
        if time2 in url:
            link = url
                
        
    print(link)

    recievers = []
    for user in User.objects.all():
        recievers.append(user.email)
        str1=" "
        string_receivers = str1.join(recievers)
        print(string_receivers)

    '''
    response = requests.get(link, stream=True)

    with open('my_image.png', 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

    img = Image.open('my_image.png')
    '''

    email_body= """<pre> 
        Congratulations! We've successfully created account.
        Go to the page: <a href={link}>click here</a>
        Thanks,
        XYZ Team.
        </pre>""".format(link= link)


    msg =MIMEText(email_body, 'html')
    msg['Subject']= 'xpto'
    msg['From']= email_user
    msg['To']=", ".join(recievers)

    '''
    message = Mail(
    from_email='goncalo_slb_matos@hotmail.com',
    to_emails='goncalomatos007@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content="""<pre> 
        Congratulations! We've successfully created account.
        Go to the page: <a href={link}>click here</a>
        Thanks,
        XYZ Team.
        </pre>""".format(link= link))
    try:
        sg = sendgrid.SendGridAPIClient(os.environ.get('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')) 
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    '''
    subject = 'Thank you from ******'
    message = 'text version of HTML message'
    from_email = 'goncalo_slb_matos@hotmail.com'
    to_list = recievers
    html_message= """<pre> 
        Congratulations! We've successfully created account.
        Go to the page: <a href={link}>click here</a>
        Thanks,
        XYZ Team.
        </pre>""".format(link= link)


    send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)
    
mailsender()