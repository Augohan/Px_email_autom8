import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from Px_email_autom8.config.settings import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL  # Update this line

# Create Email Function
def send_daily_email(subject, body, attachment_path=None):
    try:
        # Create the message container
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)

        # Establish connection to the email server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            # Send the email
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        # Optionally log the error to a file
        with open("logs/email_errors.log", "a") as log_file:
            log_file.write(f"Failed to send email. Error: {e}\n")

# Define the daily report sending function
def send_report(attachment_path=None):
    print("Generating report...")
    subject = "Go To Sleep Mafaka!"  # Updated email subject
    body = "This is the body of the daily report."
    print("Sending email...")
    send_daily_email(subject, body, attachment_path)
    print("Email sent.")
