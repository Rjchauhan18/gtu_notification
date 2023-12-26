import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

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


discord('hi', 'there')