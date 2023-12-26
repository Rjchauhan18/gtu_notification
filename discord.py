import requests
import os
from dotenv import load_dotenv
import pickle

load_dotenv('.env')

#This is just the reference and experimental file it is not connected to main.py 

def  discord(text , link):

    disc_link= os.environ['DISC_LINK']
    authorization= os.environ.get('AUTHORIZATION')

    notification= text + "\n" + link

    header = {
        "Authorization" : authorization, 
    }

    pyload = {
        "content" : notification,
    }

    r= requests.post(disc_link, pyload ,headers=header)


# discord('hi', 'there')


with open('DISCORD','rb') as f:
    r=pickle.load(f)