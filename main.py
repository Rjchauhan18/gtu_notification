import os
from os import path
import pickle
from bs4 import BeautifulSoup 
import requests
import smtplib
# from db import insert_notification,last_notification
# smtp connection

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

sender_email =os.environ.get('SMTP_SENDER_EMAIL')#sender email
smtp_password =os.environ.get('SMTP_PASSWORD')# app generated password
receiver_email = os.environ.get('SMTP_RECEIVER_EMAIL')# receiver email

# server.login(sender_email,smtp_password)
print("successful connected")

r = requests.get("https://www.gtu.ac.in/Circular.aspx")

try:
    html = BeautifulSoup(r.text,'html.parser')
except Exception as e:
    print(e)

h3_tag=html.find("h3",{"class":"d-block"})

# title and link of the content

# with open("save.txt", "r") as f:
#     last_notification = f.readlines()

#memory of code 


class Record:

    target = 'Last_notification'

if path.exists("Record"):
    # load
    print("path exits")
    with open("Record", 'rb') as f:
            recorded = pickle.load(f)
            print(recorded)

# print(recorded)

# with open("Record", 'wb') as f:
#         curr = "chauhan"
#         pickle.dump(curr, f)



def info():

    #date
    dt = (html.find("p",{"id":"ContentPlaceHolder1_lvCircular_lblUploadDate_0"})).text
    link_tag=h3_tag.find("a",{"target" :"_blank"},href=True)
    link= link_tag.get('href')

    
    print(link)
    # saved = "rahul"
    if recorded != link:
        try:
            msg = (dt + "\n\n"+link_tag.text+ "\n\n"+link + "\n")
            server.sendmail(sender_email,receiver_email,msg)
            with open("Record", 'wb') as f:
                curr = link
                pickle.dump(curr, f)
                print("link is Successfully added to code memory")
        except Exception as e:
            print("Error : ")
            print(e)
        
        
    else:
        print("No latest notification")



if __name__ == "__main__":
    info()

