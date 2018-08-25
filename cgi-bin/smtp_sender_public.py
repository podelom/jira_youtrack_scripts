#!/usr/local/bin/python3

import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.header import Header

def SendMessage(text_to_send, email):
    refused = {}
    recepients_emails = email
    gmail_sender = 'e.barnaev'
    gmail_passwd = 'Rfqhfnrth@2Mm'
    gmail_sender2 = 'e.barnaev@altatec.ru'

    msg = MIMEText(text_to_send, 'plain', 'utf-8')
    msg['Subject'] = Header('Я твоя любимая Напоминалочка', 'utf-8')
    msg['From'] = 'e.barnaev@altatec.ru'
    msg['To'] = recepients_emails

    try:
        server = smtplib.SMTP('mail.altatec.ru', 587)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        #server.set_debuglevel(1)
        server.ehlo()
        try:
            server.starttls(context=context)
            server.login(gmail_sender, gmail_passwd)
            server.sendmail(gmail_sender2, recepients_emails, msg.as_string())
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
