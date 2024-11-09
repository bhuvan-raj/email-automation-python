
# Email Automation Script

## Project Overview
This is a Python-based email automation script that sends emails at scheduled times using the Gmail SMTP server. 
The script uses the `smtplib` library to handle email sending and the `schedule` library to set up recurring email tasks. 
It can be used to send daily updates, reminders, or any automated messages.

## Features
- Sends automated emails from a Gmail account to a specified recipient.
- Allows you to schedule emails to be sent daily at a specific time.
- Secure email handling with support for Gmail App Passwords.

## Prerequisites
- **Python 3.6+**: Ensure you have Python installed. You can check this by running `python --version` in your terminal.
- **Gmail Account**: You’ll need a Gmail account to send emails. For security, it’s recommended to set up an App Password if you have two-factor authentication enabled.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/email-automation.git
   cd email-automation
   ```

2. **Install Dependencies**:
   - Install the `schedule` library using:
     ```bash
     pip install schedule
     ```

## Usage

1. **Set Up Gmail Authentication**:
   - Enable "Less secure app access" in your Google Account security settings, or generate an **App Password** if using two-factor authentication.

2. **Configure the Script**:
   - Open the `email_automation.py` file.
   - Replace the following placeholders with your details:
     ```python
     sender_email = "youremail@gmail.com"
     receiver_email = "receiveremail@example.com"
     password = "your_app_password"
     ```

3. **Run the Script**:
   - In the project directory, run:
     ```bash
     python email_automation.py
     ```
   - The script will run continuously and send an email daily at the specified time (default: 9 AM). You can adjust the schedule within the script by changing the `schedule.every().day.at("09:00").do(job)` line.

## Example Email Content
- **Subject**: Automated Email
- **Body**: "Hello, this is an automated email sent using Python!"

## Customization
- You can modify the email’s **subject** and **body** within the script by editing the `subject` and `body` variables.
- Adjust the sending time by changing `schedule.every().day.at("09:00").do(job)`.

## Troubleshooting
- **SMTP Authentication Error**: Make sure you’ve set up App Passwords if using two-factor authentication on your Gmail account.
- **Schedule Not Running**: Verify that the time format (HH:MM) in the schedule function matches your preferred sending time.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [smtplib documentation](https://docs.python.org/3/library/smtplib.html)
- [schedule library](https://pypi.org/project/schedule/)
"# email-automation-python" 
