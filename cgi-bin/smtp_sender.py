#!/usr/local/bin/python3

import smtplib
import ssl
from email.header import Header
from  email.utils import formataddr
from email.message import EmailMessage

def SendMessage(text_to_send, email):
    refused = {}
    _recepients_emails = email
    _sender_name = 'Любовь Ворклоговна'
    _sender_address = 'nadezhda_worklogovna@altatec.ru'
    _subject = 'Я - твоя любимая Напоминалочка'

    msg = EmailMessage()
    msg.set_content(text_to_send)
    msg['Subject'] = _subject
    msg['From'] = formataddr((_sender_name, _sender_address))
    msg['To'] = _recepients_emails

    try:
        server = smtplib.SMTP('mail.i.altatec.ru', 25)
        try:
            server.send_message(msg)
        finally:
              server.quit()
              print ('email sent')
    except smtplib.SMTPRecipientsRefused as e:
        refused = e.recipients
        print ('error sending mail')
    except smtplib.SMTPException as e:
        print >> 'got', e.__class__
        errcode = getattr(e, 'smtp_code', -1)
        errmsg = getattr(e, 'smtp_error', 'ignore')
        for r in rcpttos:
            refused[r] = (errcode, errmsg)
