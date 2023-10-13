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

4. **Run the Program:**
   ```bash
   python main.py
   ```
   The program will check for new notifications and send emails if needed.

Feel free to customize the configuration and adapt the program to your requirements. If you have any questions or encounter issues, please reach out to the [author](https://github.com/Rjchauhan18).
