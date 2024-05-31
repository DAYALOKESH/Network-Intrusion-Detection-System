import smtplib
import ssl
from email.mime.text import MIMEText

# Define the email sender, password, and receiver
email_sender = 'dayaduddupudi@gmail.com'
email_password = 'bzjnryjlhnuxjjfd'
email_receiver = 'jahnavi.dasari200@gmail.com'


def alert(output):
    # Set the subject of the email
    subject = 'Mail from Python'

    # Create the MIME message
    msg = MIMEText(output, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver

    # Create an SSL context outside the loop
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.ehlo()
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)
        print("Email sent")
