import os
from os import path
import pickle
from bs4 import BeautifulSoup 
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector



# Get MySQL credentials from environment variables
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']

# Connect to the MySQL database
cnx = mysql.connector.connect(
  host='3306',
  user=MYSQL_USER,
  password=MYSQL_PASSWORD,
  database='bank'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute a SELECT query
query = "SELECT * FROM gtu_notofication"
cursor.execute(query)

# Fetch the results and print them
for result in cursor.fetchall():
  print(result)

# smtp connection
def sendemail(date,Notification, link):
  # Define email addresses to use
    sender_email = os.environ.get('SMTP_SENDER_EMAIL')#sender email
    smtp_pass =os.environ.get('SMTP_PASSWORD')# app generated password
    receiver_email =os.environ.get('SMTP_RECEIVER_EMAIL')# receiver email


    # Define SMTP email server details
    smtp_server = 'smtp.gmail.com'

    # Construct email
    msg = MIMEMultipart('alternative')
    msg['To'] =receiver_email
    msg['From'] = sender_email
    msg['Subject'] = 'Latest GTU Notification'

        
    # Create the body of the message (a plain-text and an HTML version).
    html = (date + '\n'+Notification+ '\n'+link)



    part1 = MIMEText(html, 'html')

    msg.attach(part1)


    # Send the message via an SMTP server
    s = smtplib.SMTP(smtp_server,587)
    s.ehlo()
    s.starttls()
    s.login(sender_email,smtp_pass)
    print("successful connected")
    s.sendmail(sender_email, receiver_email, msg.as_string())
    s.quit()



r = requests.get("https://www.gtu.ac.in/Circular.aspx")

try:
    html = BeautifulSoup(r.text,'html.parser')
except Exception as e:
    print(e)

h3_tag=html.find("h3",{"class":"d-block"})

#memory of code 

# reading_file = open("save.txt", "r")

# t=reading_file.read()

# print(t)

class Record:

    target = 'Last_notification'

if path.exists("Record"):
    # load
    print("path exits")
    with open("Record", 'rb') as f:
            recorded = pickle.load(f)
            print("Last stored Link :"+recorded)


def info():

    #date
    dt = (html.find("p",{"id":"ContentPlaceHolder1_lvCircular_lblUploadDate_0"})).text
    link_tag=h3_tag.find("a",{"target" :"_blank"},href=True)
    link= link_tag.get('href')

    
    print("Current Link :"+link)
    if recorded != link:
        try:
            # msg = (dt + "\n\n"+link_tag.text+ "\n\n"+link + "\n")
            sendemail(dt,link_tag.text,link)
            print("Mail sended successfully")

            writitng_file = open("save.txt","w")
            
            writitng_file.write(link)
            with open("Record", 'wb') as f:
                pickle.dump(link, f)
                print("link is Successfully added to code memory")
           
        except Exception as e:
            print("Error : ")
            print(e)
        
        
    else:
        print("No latest notification")



if __name__ == "__main__":
    info()

