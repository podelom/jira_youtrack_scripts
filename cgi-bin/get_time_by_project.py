#!/usr/bin/python3

import get_worklog_altatec
import smtp_sender
import pandas as pd
import config


jira_altatec = {'e.barnaev': ['dgpbus', 'rotek', 'rustek'],
                'e.zelenov': ['dgpbus', 'DEPTRANS-RFID', 'DGPRFID', 'WH', 'VIDEOAA', 'KAMI', 'FTS', 'DOC', 'RFIDCS', 'DRFID' ]
                }
th = {
    'height': '50px',
    'width': '100px',
    'text-align': 'left'
}
prj = {}
for name in jira_altatec:
    print ("name: ", name)
    projects = [0]
    texttype = "html"
    for project in jira_altatec[name]:
        projects[0] = project
        wokrlog_today = get_worklog_altatec.Get_Today_Logged_Work(name, projects)
        prj[project] = wokrlog_today[name]
    print ("projects: ", prj)
    #content = pd.DataFrame.from_dict(prj, orient='index')
    content = pd.DataFrame(list(prj.items()), columns=['Project', 'Hours'])
    #text_to_send = content.to_html(border=0, classes='mystyle')
    #print('text_to_send = ', text_to_send)
    person = name


    HEADER = ''' 
    <html> 
        <head> 
        <style> 
        .df tbody tr:last-child { background-color: #FF0000; } 
        </style> 
        </head> 
        <body> 
    ''' 
    FOOTER = ''' 
        </body> 
    </html> 
    ''' 
    with open('test.html', 'w') as f:
        f.write(HEADER) 
        f.write(content.to_html(classes='df')) 
        f.write(FOOTER) 
        f.close()
    with open('test.html', 'r') as f:
        text_to_send = f.read()


    smtp_sender.SendMessage(text_to_send, config.emails[person], texttype)
