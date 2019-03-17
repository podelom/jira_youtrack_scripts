#!/usr/bin/python3

import json
import logging

import smtp_sender
import get_worklog_jira_1
import get_worklog_jira_2
import text_data_prod
import config_prod
#import get_worklog_youtrack
#import config_template

#logging
logger = logging.getLogger("todayWorklogReminder")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("worklogReminder.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == "__main__":
    print ("I'm here")
    jira_2 = config_prod.jira_2
    jira_1 = config_prod.jira_1
    #youtrack_tkp = config_prod.youtrack_tkp
    template = text_data_prod
    summary = {}
    texttype = "plain"
    for name in jira_2:
        person = name
        projects = jira_2[name]
        dgp_worklog_today = get_worklog_jira_2.Get_Today_Logged_Work(person, projects)
        if person in summary:
            summary[person] += dgp_worklog_today[person]
        else:
            summary.update(dgp_worklog_today)

    for name in jira_1:
        person = name
        projects = jira_1[name]
        altatec_worklog_today = get_worklog_jira_1.Get_Today_Logged_Work(person, projects)
        if person in summary:
            summary[person] += altatec_worklog_today[person]
        else:
            summary.update(altatec_worklog_today)

    '''
    for name in youtrack_tkp:
        person = name
        projects = youtrack_tkp[name]
        print("projects: ", projects)
        print("person: ", person)
        tkp_worklog_today = get_worklog_youtrack.Get_Today_Logged_Work(person, projects)
        print ("tkp_worklog_today", tkp_worklog_today)
        if person in summary:
            summary[person] += tkp_worklog_today[person]
        else:
            summary.update(altatec_worklog_today)
        '''
    for person in summary:
        print ("Person: ", person, " - " ,summary[person])
        if summary[person] == 0:
            if person in config_prod.emails:
                for item in config_prod.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = template.today_log0['nojoke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = template.today_log0['nojoke_w'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = template.today_log0['joke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = template.today_log0['joke_w'].format(summary[person])
                        print ("name: ", item['name']) 
                        break
                logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                smtp_sender.SendMessage(text_to_send, config_prod.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 0 and summary[person] <= 3):
            if person in config_prod.emails:
                for item in config_prod.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = template.today_log0_3['nojoke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = template.today_log0_3['nojoke_w'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = template.today_log0_3['joke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = template.today_log0_3['joke_w'].format(summary[person])
                        print ("name: ", item['name']) 
                        break
                logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                smtp_sender.SendMessage(text_to_send, config_prod.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] < 8):
            if person in config_prod.emails:
                for item in config_prod.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = template.today_log3_8['nojoke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = template.today_log3_8['nojoke_w'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = template.today_log3_8['joke'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = template.today_log3_8['joke_w'].format(summary[person])
                        print ("name: ", item['name']) 
                        break
                logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                smtp_sender.SendMessage(text_to_send, config_prod.emails[person], texttype)
            else: print ("no email")
        elif summary[person] >= 8:
            if person in config_prod.emails:
                for item in config_prod.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = template.today_log8['nojoke'].format(summary[person])
                        print ("Человек несмеющийся: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = template.today_log8['nojoke_w'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = template.today_log8['joke'].format(summary[person])
                        print ("Человек несмеющийся: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = template.today_log8['joke_w'].format(summary[person])
                        print ("name: ", item['name'])
                        break
                logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                smtp_sender.SendMessage(text_to_send, config_prod.emails[person], texttype)
            else: print ("no email")
    
    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, config_prod.email_report, texttype)
