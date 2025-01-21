import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import imaplib
import email
from imapclient import IMAPClient

# pip install --user smtplib email imapclient

# Email configuration
EMAIL_SERVER_USER = 'gaialover@gmail.com'
EMAIL_SERVER_PASSWORD = 'rahasia'
EMAIL_SERVER_HOST = 'smtp.gmail.com'
EMAIL_SERVER_PORT = 465
EMAIL_FROM = 'gaialover@gmail.com'

def send_email2(to, subject, body, attachment=None):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = to
    msg['Subject'] = subject

    # Attach body as HTML, Markdown, or plain text
    if body.lower().endswith('.md'):
        with open(body, 'r') as file:
            body_content = file.read()
        body_part = MIMEText(body_content, 'markdown')
    elif body.lower().endswith('.html'):
        with open(body, 'r') as file:
            body_content = file.read()
        body_part = MIMEText(body_content, 'html')
    else:
        body_part = MIMEText(body, 'plain')

    msg.attach(body_part)

    # Attach file if specified
    if attachment:
        with open(attachment, 'rb') as file:
            attachment_part = MIMEApplication(file.read(), Name=attachment)
        attachment_part['Content-Disposition'] = f'attachment; filename="{attachment}"'
        msg.attach(attachment_part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) as server:
        server.login(EMAIL_SERVER_USER, EMAIL_SERVER_PASSWORD)
        server.sendmail(EMAIL_FROM, to, msg.as_string())


def test_send_email():
    # Example usage:
    to_email = 'recipient@example.com'
    email_subject = 'Test Email'
    email_body = 'This is a test email body in plain text.'
    attachment_path = 'path/to/attachment.txt'
    send_email2(to_email, email_subject, email_body, attachment_path)


# User
# i want to create a fullstack email application where i have to provide all kinds of email functionalities.
# the backend would use python, but at this point, i just want to write as much as possible, python functions related to email, so it will help my work later on.
# give me those functions.

# ChatGPT
# Creating a full-stack email application is a significant task that involves both front-end and back-end development. For the back-end, you'll likely want to use a web framework like Flask or Django in Python. Below, I'll provide you with some example Python functions that you might find useful for handling email-related functionalities in the backend. These are just basic examples, and you'll need to integrate them into your web framework and adapt them to your specific needs.

# Sending Email:
def send_email(to_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    from_email = "your_email@example.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())

# Receiving Email (IMAP):
def read_emails(imap_server, imap_port, username, password):
    with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
        mail.login(username, password)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        message_ids = messages[0].split()

        for message_id in message_ids:
            _, msg_data = mail.fetch(message_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            print("Subject:", msg["Subject"])
            print("From:", msg["From"])
            print("Date:", msg["Date"])
            print("Body:", msg.get_payload())

# Fetching Email Attachments:
def download_attachments(imap_server, imap_port, username, password, message_id, download_path):
    with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
        mail.login(username, password)
        mail.select("inbox")

        _, msg_data = mail.fetch(message_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        for part in msg.walk():
            if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename:
                with open(f"{download_path}/{filename}", "wb") as f:
                    f.write(part.get_payload(decode=True))

# Creating Drafts:
def create_draft(imap_server, imap_port, username, password, to_email, subject, message):
    with IMAPClient(imap_server) as client:
        client.login(username, password)
        client.select_folder("Drafts")

        draft = MIMEMultipart()
        draft['To'] = to_email
        draft['Subject'] = subject
        draft.attach(MIMEText(message, 'plain'))

        client.append("Drafts", draft.as_bytes(), [b'\\Draft'])

# Remember to install necessary libraries if you haven't already:

# pip install smtplib email imapclient

# These are just starting points, and you'll likely need to modify and expand upon them based on the specific requirements of your application. Additionally, consider handling exceptions, security measures (e.g., storing passwords securely), and other aspects based on your application's needs.
