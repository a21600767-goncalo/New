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




'''
    time_today = datetime.now()

    time_x = time_today + timedelta(days=+2) 

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

    x = name[1]

    print(item)
    
'''   


    

access_token ="EAAEZAZAyZC4tuYBAAocZAbS2Vh5yWR5Oy6rkBXfrZAU5ffZBajum2WzVocQ5QV9Hucjfc146GaK3fm3hO8Hy52ITx0svfqIMTqdkWhfg2z7KohOSWBknpSoHyn2KdvXkItmA9vKjKBW48Xs2XKZAn6a9sfthQ3jR3V32ETthH19IjWpDTRWL4wo";

facebook = fb.GraphAPI(access_token)

facebook.put_object('me', 'feed', message="Just posting something on my wall")
    



