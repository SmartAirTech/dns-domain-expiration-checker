#!/usr/bin/env python3
"""
Send domain expiration report via AWS SES SMTP
"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(smtp_server, smtp_port, username, password,
                                email_from, email_to, subject, body, attachment_path):
    """Send email with attachment via SMTP"""
    try:
        print(f'Connecting to {smtp_server}:{smtp_port}...')
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        print('Logging in...')
        server.login(username, password)

        # Create message
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = subject

        # Add body
        msg.attach(MIMEText(body, 'plain'))

        # Add attachment if file exists
        if os.path.exists(attachment_path):
            print(f'Attaching {attachment_path}...')
            with open(attachment_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                              f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(part)
        else:
            print(f'Warning: Attachment {attachment_path} not found')

        # Send email
        print('Sending email...')
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()

        print(f'✅ SUCCESS! Email sent to {email_to}')
        return 0

    except Exception as e:
        print(f'❌ ERROR: {e}')
        return 1

if __name__ == '__main__':
    # Get credentials from environment variables
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    username = os.environ.get('SMTP_USERNAME')
    password = os.environ.get('SMTP_PASSWORD')
    email_from = os.environ.get('EMAIL_FROM')
    email_to = os.environ.get('EMAIL_TO')
    subject = os.environ.get('EMAIL_SUBJECT', 'Domain Expiration Report')
    body = os.environ.get('EMAIL_BODY', 'See attached report.')
    attachment = os.environ.get('ATTACHMENT_PATH', 'domain_report.txt')

    # Validate required variables
    required = {
        'SMTP_SERVER': smtp_server,
        'SMTP_USERNAME': username,
        'SMTP_PASSWORD': password,
        'EMAIL_FROM': email_from,
        'EMAIL_TO': email_to
    }

    missing = [k for k, v in required.items() if not v]
    if missing:
        print(f'❌ ERROR: Missing required environment variables: {", ".join(missing)}')
        sys.exit(1)

    sys.exit(send_email_with_attachment(
        smtp_server, smtp_port, username, password,
        email_from, email_to, subject, body, attachment
    ))
