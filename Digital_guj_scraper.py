import requests
import json
from bs4 import BeautifulSoup
import os
from os import path
import pickle
from bs4 import BeautifulSoup 
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date


# smtp connection
def Sendemail(date,Notification, link):
  # Define email addresses to use
    sender_email =os.environ.get('SMTP_SENDER_EMAIL')#sender email
    smtp_pass = os.environ.get('SMTP_PASSWORD')# app generated password
    receivers_email =os.environ.get('SMTP_RECEIVER_EMAIL')# receiver email


    # Define SMTP email server details
    smtp_server = 'smtp.gmail.com'

    # Construct email
    msg = MIMEMultipart('alternative')
    msg['To'] =receivers_email
    msg['From'] = sender_email
    msg['Subject'] = 'Latest GTU Notification'

    # Create the body of the message (a plain-text and an HTML version).
    html = (str(date) + '\n'+Notification+ '\n'+link)



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

# load notifs from json
def load_notifications(filename):
    try:
        with open(filename, 'r') as file:
            notifications = json.load(file)
        if not isinstance(notifications, list):
            raise ValueError("Invalid data format in JSON file")
        return notifications
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []

# save notifs to json
def save_notifications(notifications, filename):
    with open(filename, 'w') as file:
        json.dump(notifications, file)

url = 'https://www.digitalgujarat.gov.in/loginapp/CitizenLogin.aspx'
if __name__ == '__main__':
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    tr_tags = soup.find_all('tr')

    # Load existing notifications from the JSON file
    filename = 'notifications.json'
    existing_notifications = load_notifications(filename)

    new_notifications = []

    for tr_tag in tr_tags:
        a_tags = tr_tag.find_all('td')[1].find('span').find_all('a')
        formatted_content = []
        
        for a_tag in a_tags:
            link_text = a_tag.text.strip()
            link_href = a_tag.get('href', '').strip()
            if link_href:
                formatted_link = f"<a href='{url + link_href}'>{link_text}</a>"
                formatted_content.append(formatted_link)
            else:
                formatted_content.append(link_text)
        notification_text = '<br><br> '.join(formatted_content)
        
        # Check if the notification is new 
        if notification_text not in existing_notifications:
            # Add the new notification to the list of new notifications
            new_notifications.append(notification_text)

    existing_notifications = new_notifications + existing_notifications

    # Save the updated notifications to the JSON file
    save_notifications(existing_notifications, filename)

    # email
    if new_notifications:
        new_notifications_text = '\n'.join(new_notifications)
        print(f"Sending email for new notifications:\n{new_notifications_text}")
        today = date.today()
        Sendemail(today, new_notifications_text, url)
    else:
        print("No new notifications to send.")