## GTU-NOTIFICATION

### Description

This program checks the GTU website: https://www.gtu.ac.in for new notifications and sends an email to a list of people if a new notification is found. It utilizes a web-scraping library to extract notification information and sends the email. The program also keeps track of the link to the last notification, ensuring it checks for new notifications since the last run.

### Language

- Python

### Author

- @Rjchauhan18: https://github.com/Rjchauhan18

### License

MIT LICENSE: LICENSE

### Setup and Usage

To set up and use this project locally, follow these steps:

1. **Clone the Repository:**

```bash
git clone https://github.com/Rjchauhan18/gtu_notification.git
cd gtu_notification
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure Email Credentials:**

Create a `.env` file in the project root directory and add the following lines:

```
SMTP_SENDER_EMAIL="your sender email"
SMPT_PASSWORD="Your SMTP app password"
```

4. **SMTP Setup:**

If you are using Gmail, follow these steps to generate an App Password for SMTP:

1. Go to your Google Account: https://myaccount.google.com/.
2. Navigate to the "Security" section.
3. Under "Signing in to Google," select "App passwords."
4. Select "Mail" from the drop-down menu and click "Generate."
5. Enter a name for the app and click "Generate."
6. Copy the 16-digit App Password and paste it into the `.env` file.

5. **Run the Program:**
```
python main.py
```

The program will check for new notifications and send emails if needed.

### Screenshots

#### Generating an App Password
<img src='https://www.chatwoot.com/docs/assets/images/sign_in_google-e7b0d4d6f440f757f5158b84ba28bd18.png' >

#### Entering the App Password
<img src='https://www.chatwoot.com/docs/assets/images/generate_password-5ef020ff5cd15276065f721667357ad9.gif' >

### Customization

Feel free to customize the configuration and adapt the program to your requirements. For example, you can change the following:

* The email sender and recipient addresses
* The frequency at which the program checks for new notifications
* The content of the email notification

### Support

If you have any questions or encounter issues, please reach out to the author: https://github.com/Rjchauhan18.
