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
def Sendemail(date,Notification, link,receivers_email):
  # Define email addresses to use
    sender_email = os.environ.get('SMTP_SENDER_EMAIL')#sender email
    smtp_pass = os.environ.get('SMTP_PASSWORD')# app generated password
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
    html = (date + '\n'+Notification+ '\n'+link)



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
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')


tr_tags = soup.find_all('tr')

# Load existing notifications from the JSON file
filename = 'notifications.json'
existing_notifications = load_notifications(filename)

new_notifications = []

# Loop through each <tr> tag and extract the text and links from the specified structure
for tr_tag in tr_tags:
    # Find all <a> tags inside the <span> tag in the 2nd <td> tag of the current <tr> tag
    a_tags = tr_tag.find_all('td')[1].find('span').find_all('a')
    
    # Initialize an empty list to store formatted content for the current notification
    formatted_content = []
    
    # Loop through <a> tags and add text or formatted links based on presence of href attribute
    for a_tag in a_tags:
        link_text = a_tag.text.strip()
        link_href = a_tag.get('href', '').strip()
        if link_href:
            # Format the hyperlink in the desired format
            formatted_link = f"<a href='{url + link_href}'>{link_text}</a>"
            formatted_content.append(formatted_link)
        else:
            # If no href attribute, add plain text to the formatted content list
            formatted_content.append(link_text)
    
    # Join the formatted content list into a single string for the current notification
    notification_text = ' '.join(formatted_content)
    
    # Check if the notification is new (not in existing notifications)
    if notification_text not in existing_notifications:
        # Add the new notification to the list of new notifications
        new_notifications.append(notification_text)

# Add new notifications to the beginning of the existing notifications list
existing_notifications = new_notifications + existing_notifications

# Save the updated notifications to the JSON file
save_notifications(existing_notifications, filename)

# email
if new_notifications:
    new_notifications_text = '\n'.join(new_notifications)
    # print(f"Sending email for new notifications:\n{new_notifications_text}")
    receivers_email="ENTER RECIEVER MAIL ID"
    today = date.today()
    Sendemail(today, new_notifications_text, url,receivers_email)
else:
    print("No new notifications to send.")