#!/usr/local/bin/python3

import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.header import Header
import securer_prod
import smtp_details_prod

smtp_server = securer_prod.smtp_server_public
template = smtp_details_prod.tmpl1
def SendMessage(text_to_send, email):
    refused = {}
    recepients_emails = email
    mail_login = smtp_server['login']
    mail_passwd = smtp_server['password']
    mail_sender = smtp_server['sender']

    msg = MIMEText(text_to_send, 'plain', 'utf-8')
    msg['Subject'] = Header(template['subject'], 'utf-8')
    msg['From'] = mail_sender
    msg['To'] = recepients_emails

    try:
        server = smtplib.SMTP(smtp_server['link'], 587)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        #server.set_debuglevel(1)
        server.ehlo()
        try:
            server.starttls(context=context)
            server.login(mail_login, mail_passwd)
            server.sendmail(mail_sender, recepients_emails, msg.as_string())
        finally:
              #print(msg)
              server.quit()
              print ('email sent')
    except smtplib.SMTPRecipientsRefused as e:
        print >> DEBUGSTREAM, 'got SMTPRecipientsRefused'
        refused = e.recipients
        print ('error sending mail')
    except smtplib.SMTPException as e:
        print >> DEBUGSTREAM, 'got', e.__class__
        errcode = getattr(e, 'smtp_code', -1)
        errmsg = getattr(e, 'smtp_error', 'ignore')
        for r in rcpttos:
            refused[r] = (errcode, errmsg)
