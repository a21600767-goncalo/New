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
        api_secret = "qt3MG0N2omjL_7kS_khMi7k5_1c"                      #cloudinary config
        )

        tag ='evento-canvas'                                            #tag used to search through cloud's directories 

        time_today = datetime.now()                                     #actual time

        time_x = time_today + timedelta(days=-21)                        #time(in days) we want to search through the list of canvas in cloud

        time2 = time_x.strftime("%Y-%m-%d")                             #we had to format time to "YYYY-MM-DD" in order to match canvas names

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



        access_token ="EAAEZAZAyZC4tuYBAAocZAbS2Vh5yWR5Oy6rkBXfrZAU5ffZBajum2WzVocQ5QV9Hucjfc146GaK3fm3hO8Hy52ITx0svfqIMTqdkWhfg2z7KohOSWBknpSoHyn2KdvXkItmA9vKjKBW48Xs2XKZAn6a9sfthQ3jR3V32ETthH19IjWpDTRWL4wo";

        #facebook access token

        facebook = fb.GraphAPI(access_token)                          

        facebook.put_photo(urllib.request.urlopen(link))    

post()