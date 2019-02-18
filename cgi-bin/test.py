#!/usr/local/bin/python3

import get_worklog_altatec
import get_worklog_dgp
import config
import smtp_sender
import json

#text_to_send = "Чмафки!"
#email = 'e.barnaev@altatec.ru'
#smtp_sender.SendMessage(text_to_send, 'e.barnaev@altatec.ru')

param = 'a.sheviakov'
print (config.employee[param])