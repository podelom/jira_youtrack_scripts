#!/usr/bin/python3

import json
import logging


import smtp_sender
import text_data_templates
import config_templates
import get_worklog_jira_1
import get_worklog_jira_2
#import get_worklog_youtrack

#logging
logger = logging.getLogger("yesterdayWorklogReminder")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("worklogReminder.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == "__main__":
    jira_dgp = config_templates.jira_2
    jira_altatec = config_templates.jira_1
    #youtrack_tkp = config_templates.youtrack_tkp
    template = text_data_templates
    summary = {}
    texttype = "plain"
    for name in jira_dgp:
        person = name
        projects = jira_dgp[name]
        dgp_worklog_today = get_worklog_jira_2.Get_Yesterday_Logged_Work(person, projects)
        if person in summary:
            summary[person] += dgp_worklog_today[person]
        else:
            summary.update(dgp_worklog_today)

    for name in jira_altatec:
        person = name
        projects = jira_altatec[name]
        altatec_worklog_today = get_worklog_jira_1.Get_Yesterday_Logged_Work(person, projects)
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
        tkp_worklog_today = get_worklog_youtrack.Get_Yesterday_Logged_Work(person, projects)
        print ("tkp_worklog_today", tkp_worklog_today)
        if person in summary:
            summary[person] += tkp_worklog_today[person]
        else:
            summary.update(altatec_worklog_today)
    '''
    for person in summary:
        print ("Person: ", person)
        if summary[person] == 0:
            if person in config_templates.emails:
                for name in config_templates.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log0['nojoke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log0['nojoke_w'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log0['joke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log0['joke_w'].format(summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: 
                        print ("no employee: ", person)
                        logger.warning("{} is not in the list and will not receive any worklog".format(person))
                        text_to_send = ""
                if text_to_send != "":
                    logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                    smtp_sender.SendMessage(text_to_send, config_templates.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 0 and summary[person] <= 3):
            if person in config_templates.emails:
                for name in config_templates.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log0_3['nojoke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log0_3['nojoke_w'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log0_3['joke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log0_3['joke_w'].format(summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: 
                        print ("no employee: ", person)
                        logger.warning("{} is not in the list and will not receive any worklog".format(person))
                        text_to_send = ""
                if text_to_send != "":
                    logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                    smtp_sender.SendMessage(text_to_send, config_templates.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] < 8):
            if person in config_templates.emails:
                for name in config_templates.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log3_8['nojoke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log3_8['nojoke_w'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log3_8['joke'].format(summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log3_8['joke_w'].format(summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: 
                        print ("no employee: ", person)
                        logger.warning("{} is not in the list and will not receive any worklog".format(person))
                        text_to_send = ""
                if text_to_send != "":
                    logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                    smtp_sender.SendMessage(text_to_send, config_templates.emails[person], texttype)
            else: print ("no email")
        elif summary[person] >= 8:
            if person in config_templates.emails:
                for name in config_templates.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log8['nojoke'].format(summary[person])
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = template.yesterday_log8['nojoke_w'].format(summary[person])
                        print ("name: ", name['name'])
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log8['joke'].format(summary[person])
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = template.yesterday_log8['joke_w'].format(summary[person])
                        print ("name: ", name['name'])
                    else: 
                        print ("no employee: ", person)
                        logger.warning("{} is not in the list and will not receive any worklog".format(person))
                        text_to_send = ""
                if text_to_send != "":
                    logger.info("Text to send: {}, person to recieve: {}".format(text_to_send, person))
                    smtp_sender.SendMessage(text_to_send, config_templates.emails[person], texttype)
            else: print ("no email")

    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, config_templates.email_report, texttype)
