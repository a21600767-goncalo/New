
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

    email_user = 'goncalomatos007@gmail.com'                            #email credentials 
    email_password = 'SUpertramp007'

    cloudinary.config( 
        cloud_name = "da7qp20ja",                                       #cloudinary config
        api_key = "835922641349356", 
        api_secret = "qt3MG0N2omjL_7kS_khMi7k5_1c"
        )

    tag ='evento-canvas'                                                #tag used to search through cloud's directories 

    time_today = datetime.now()                                         #actual time

    time_x = time_today + timedelta(days=-16)                           #time(in days) we want to search through the list of canvas in cloud 

    time2 = time_x.strftime("%Y-%m-%d")                                 #we had to format time to "YYYY-MM-DD" in order to match canvas names

    result = cloudinary.Search()\
    .expression(tag)\
    .execute()
                                                                        #we used an api from cloudinary that is able to search through the cloud's directories, it returns an JSON response 
    
    cloud = 'http://res.cloudinary.com/da7qp20ja/image/upload/'
            
    json_response = json.dumps(result)
    json_response_to_string = ''.join(json_response)
    stripped_string = json_response_to_string.replace('"', '')
    json_response_to_list = list(json_response.split(' '))
                                                                
                                                                        #here we converted json response to string and then to a list of string elements 
   
    urls =[[a] for a in json_response_to_list if cloud in a]
    urls2 = [''.join(ele) for ele in urls]
    urls3 = ''.join(urls2)
    urls4 = urls3.replace('"', '')                                      # here we search through the list of string elements from json response, if there is an item that matches the cloud url we save it into a list
    urls_list = list(urls4.split(","))


    


    print(urls)

    url=""
    link =""
    for url in urls_list:                                               #here we make a match between urls and time that we set earlier, and after that we have the canvas url
        if time2 in url:
            link = url
                
        
    print(link)

    recievers = []
    for user in User.objects.all():
        recievers.append(user.email)                                    #here we get all emails saved on database and copy them to a string 
        str1=" "
        string_receivers = str1.join(recievers)
        print(string_receivers)

    

        #here we have an email body(html with string format) with a link to canvas


    msg =MIMEText(email_body, 'html')
    msg['Subject']= 'xpto'
    msg['From']= email_user
    msg['To']=", ".join(recievers)

    subject = 'Thank you from ******'
    message = 'text version of HTML message'
    from_email = 'goncalo_slb_matos@hotmail.com'
    to_list = recievers
    html_message= """<pre> 
        Congratulations! We've successfully created account.
        Go to the page: <a href={link}>click here</a>
        Thanks,
        XYZ Team.                                           #here we have an email body(html with string format) with a link to canvas
        </pre>""".format(link= link)


    send_mail(subject,message,from_email,to_list,fail_silently=True,html_message=html_message)   #message sent 
    
mailsender()