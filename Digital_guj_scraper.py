import os
import requests 
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def information():
    r= requests.get("https://www.digitalgujarat.gov.in/loginapp/CitizenLogin.aspx")
    html = BeautifulSoup(r.text,'html.parser')


    table = html.select('table')[0] 
    TR=table.find_all('tr')
    
    with open("datafile.txt","r") as f:
        last_data=f.read()
    last_data_list=last_data.split('\n')
    last_data=[x for x in last_data_list if x!=""]
    print(last_data[0])
    print(TR[0].text)
    if last_data[0]==TR[0].text:
        print(True)
    else:
        print(False)
    
    if last_data[0]==TR[0].text or last_data[1]==TR[1].text:
        print("no change")
    else:
        with open("datafile.txt","w") as f:
           
                # print(i.text)
            f.write(TR[0].text)

            f.write("\n")

            f.write(TR[1].text)
            f.write("\n")
            
            print("added")
                    
    


def Sendemail(date,receivers_email):
  # Define email addresses to use
    sender_email =os.environ.get('SMTP_SENDER_EMAIL')#sender email
    smtp_pass = os.environ.get('SMTP_PASSWORD')# app generated password
    # print(sender_email)
    # print(smtp_pass)
    # print(receivers_email)
    # receivers_email =os.environ.get('SMTP_RECEIVER_EMAIL')# receiver email


    # Define SMTP email server details
    smtp_server = 'smtp.gmail.com'

    # Construct email
    msg = MIMEMultipart('alternative')
    msg['To'] =receivers_email
    msg['From'] = sender_email
    msg['Subject'] = 'Latest GTU Notification'

    # Create the body of the message (a plain-text and an HTML version).
    # html = (date + '\n'+Notification+ '\n'+link)
    html = (date )




    part1 = MIMEText(html, 'html')

    msg.attach(part1)

    # Send the message via an SMTP server
    s = smtplib.SMTP(smtp_server,587)
    s.ehlo()
    s.starttls()
    s.login(sender_email,smtp_pass)
    print("successful connected")
    s.sendmail(sender_email, receivers_email, msg.as_string())
    s.quit()

if __name__ == '__main__':
    information()