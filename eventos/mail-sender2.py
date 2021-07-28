
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

    time_x = time_today + timedelta(days=+1) 

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
        print(recievers)


    response = requests.get(link, stream=True)

    with open('my_image.png', 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

    img = Image.open('my_image.png')
    
    msg = EmailMessage()
    msg['Subject']= 'xpto'
    msg['From']= email_user
    msg['To']=recievers
    msg.set_content('Este é o nosso proximo evento!!')

    with open('my_image.png', 'rb') as fp:
        img_data = fp.read()
        file_type= imghdr.what(fp.name)
        file_name=fp.name
        msg.add_attachment(img_data, maintype='image',
            subtype=file_type, filename=file_name)


    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_user, email_password)
        
        smtp.send_message(msg)
    
mailsender()