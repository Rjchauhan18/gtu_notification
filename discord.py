import requests 
import os

link= os.environ.get('DISC_LINK')
authorization= os.environ.get('AUTHORIZATION')

def  discord(notification):

    header = {
        "Authorization" : authorization, 
    }

    pyload = {
        "content" : notification,
    }

    r= requests.post(link, pyload ,headers=header)