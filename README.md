
# GTU-NOTIFICATION

[![GTU-NOTIFICATION](https://github.com/Rjchauhan18/gtu_notification/actions/workflows/actions.yml/badge.svg)](https://github.com/Rjchauhan18/gtu_notification/actions/workflows/actions.yml)
[![CodeQL](https://github.com/Rjchauhan18/gtu_notification/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Rjchauhan18/gtu_notification/actions/workflows/github-code-scanning/codeql)

## Description

This program checks the [GTU website](https://www.gtu.ac.in) for new notifications and sends an email to a list of people if a new notification is found. It utilizes a web-scraping library to extract notification information and sends the email. The program also keeps track of the link to the last notification, ensuring it checks for new notifications since the last run.

## Language

- Python

## Author

- [@Rjchauhan18](https://github.com/Rjchauhan18)

## License

[MIT LICENSE](LICENSE)

## Setup and Usage

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
   Open the `config.py` file and provide your email credentials.

   ```python
   # config.py

   EMAIL_CONFIG = {
       'sender_email': 'your-email@gmail.com',
       'sender_password': 'your-email-password',
       'receiver_emails': ['recipient1@example.com', 'recipient2@example.com'],
   }
   ```

4. **SMTP Setup:**

   This program utilizes SMTP for sending emails. Follow the steps below to set up SMTP and obtain an App Password if needed.

   - **Configure SMTP Settings:**
     Open the `config.py` file and provide the required SMTP configuration parameters.

     ```python
     # config.py

     SMTP_CONFIG = {
         'smtp_host': 'your-smtp-host',
         'smtp_port': 587,  # or your SMTP port
         'smtp_secure': False,  # set to True if using SSL
     }
     ```

   - **Get App Password for SMTP:**
     If you are using services like Gmail, you may need to generate an "App Password" for secure authentication.
     
     - **For Gmail:**
       1. Go to your [Google Account](https://myaccount.google.com/).
       2. Navigate to the "Security" section.
       3. Under "Signing in to Google," select "App passwords."
       4. Generate a new App Password for your application.

     Replace `'your-smtp-host'` in `config.py` with the appropriate SMTP host and update other configurations accordingly.

   - **Save Changes and Restart:**
     Save the changes to the `config.py` file and restart the application.

     ```bash
     python main.py
     ```

5. **Run the Program:**
   ```bash
   python main.py
   ```
   The program will check for new notifications and send emails if needed.

Feel free to customize the configuration and adapt the program to your requirements. If you have any questions or encounter issues, please reach out to the [author](https://github.com/Rjchauhan18).
