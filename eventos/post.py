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




def post():
        
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




        access_token ="EAAEZAZAyZC4tuYBAAocZAbS2Vh5yWR5Oy6rkBXfrZAU5ffZBajum2WzVocQ5QV9Hucjfc146GaK3fm3hO8Hy52ITx0svfqIMTqdkWhfg2z7KohOSWBknpSoHyn2KdvXkItmA9vKjKBW48Xs2XKZAn6a9sfthQ3jR3V32ETthH19IjWpDTRWL4wo";

        facebook = fb.GraphAPI(access_token)

        facebook.put_photo(urllib.request.urlopen(link))    

post()