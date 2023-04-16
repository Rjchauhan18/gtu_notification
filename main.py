import os
from bs4 import BeautifulSoup 
import requests
import time 
import smtplib

# smtp connection

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
sender_email = os.environ.get('SMTP_SENDER_EMAIL')
smtp_password =  os.environ.get('SMTP_PASSWORD')
receiver_email =  os.environ.get('SMTP_RECEIVER_EMAIL')

server.login(sender_email,smtp_password)
print("successful connected")

r = requests.get("https://www.gtu.ac.in/Circular.aspx")

try:
    html = BeautifulSoup(r.text,'html.parser')
except Exception as e:
    print(e)

h3_tag=html.find("h3",{"class":"d-block"})

# title and link of the content

with open("save.txt", "r") as f:
    last_notification = f.readlines()


def info():

    #date
    dt = (html.find("p",{"id":"ContentPlaceHolder1_lvCircular_lblUploadDate_0"})).text
    link_tag=h3_tag.find("a",{"target" :"_blank"},href=True)
    link= link_tag.get('href')

    if last_notification[0] != link:
        try:
            msg = (dt + "\n\n"+link_tag.text+ "\n\n"+link + "\n")
            server.sendmail(sender_email,receiver_email,msg)
        except Exception as e:
            print(e)

        with open("save.txt", "w") as f:
            f.writelines(link)
            print("Successfully written in save.txt file")
    else:
        print("No latest notification")



if __name__ == "__main__":
    info()

