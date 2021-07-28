import os
import re
import requests
import facebook as fb
import glob
from datetime import datetime, timedelta, time
import schedule
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json


def post_canvas():

    cloudinary.config( 
    cloud_name = "da7qp20ja", 
    api_key = "835922641349356", 
    api_secret = "qt3MG0N2omjL_7kS_khMi7k5_1c" 
)
    w ='evento-canvas'

    time_today = datetime.now()

    time_x = time_today + timedelta(days=+3) 

    time2 = time_x.strftime("%Y-%m-%d")

    canvas_list = glob.glob('C:/Users/gonca/Downloads/*evento-canvas*')                  
    
    canvas= ""
    item =""
    for canvas in canvas_list:
        if time2 in canvas:
            item = canvas
            break
        
            
    
    string = ''.join(item)

    print(string)

    name = string.split('\\')

    print(name[1])

    tag = name[1]

    print(canvas_list)
    
    canvas_list2 =[[element] for element in canvas_list]
    
    
    
    
    print(string)
    
    
    cloudinary.uploader.upload(string, tag= w, folder="Canvas")
    
    
post_canvas()


