Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import smtplib
... import schedule
... import time
... 
... def send_email():
...     # Set up email sender and receiver
...     sender_email = "bhuvanraj@gmail.com"
...     receiver_email = "testreceive@gmail.com"
...     password = "Bhuvanraj123"  # Use your Gmail App Password if 2FA is enabled
... 
...     # Create the email content
...     subject = "Automated Email"
...     body = "Hello, this is an automated email sent using Python!"
...     email_text = f"Subject: {subject}\n\n{body}"
... 
...     try:
...         # Set up the Gmail SMTP server
...         server = smtplib.SMTP('smtp.gmail.com', 587)
...         server.starttls()  # Secure the connection
...         server.login(sender_email, password)  # Log in to the email account
...         
...         # Send the email
...         server.sendmail(sender_email, receiver_email, email_text)
...         print("Email sent successfully!")
... 
...     except Exception as e:
...         print(f"Error: {e}")
... 
...     finally:
...         # Disconnect from the server
...         server.quit()
... 
... # Schedule the email to be sent daily at 9 AM
... schedule.every().day.at("09:00").do(send_email)
... 
... print("Email scheduling script running...")
... 
... # Keep the script running
... while True:
...     schedule.run_pending()
...     time.sleep(60)  # Check every minute
