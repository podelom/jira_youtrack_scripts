#!/usr/local/bin/python3

import smtplib
import ssl
from email.header import Header
from  email.utils import formataddr
from email.message import EmailMessage
import securer_templates
import smtp_details_templates_templates_templates_templates_prod

smtp_server = securer_templates.smtp_server['link']
template = smtp_details_templates_templates_templates_templates_prod.tmpl1
def SendMessage(text_to_send, email, texttype):
    refused = {}
    recepients_emails = email
    sender_name = template['sender_name']
    sender_address = template['sender_address']
    subject = template['subject']

    msg = EmailMessage()
    msg.set_content(text_to_send, subtype=texttype)
    msg['Subject'] = subject
    msg['From'] = formataddr((sender_name, sender_address))
    msg['To'] = recepients_emails

    try:
        server = smtplib.SMTP(smtp_server, 25)
        try:
            server.send_message(msg)
        finally:
              server.quit()
              print ('email sent')
    except smtplib.SMTPRecipientsRefused as e:
        refused = e.recipients
        print ('error sending mail')
    except smtplib.SMTPException as e:
        print ('got', e.__class__)
        errcode = getattr(e, 'smtp_code', -1)
        errmsg = getattr(e, 'smtp_error', 'ignore')
        for r in rcpttos:
            refused[r] = (errcode, errmsg)
