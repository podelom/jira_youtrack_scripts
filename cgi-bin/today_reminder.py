#!/usr/bin/python3

import get_worklog_altatec
import get_worklog_dgp
#import get_worklog_youtrack
import config
import smtp_sender
import json

if __name__ == "__main__":
    print ("I'm here")
    jira_dgp = config.jira_dgp
    jira_altatec = config.jira_altatec
    #youtrack_tkp = config.youtrack_tkp
    summary = {}
    texttype = "plain"
    for name in jira_dgp:
        person = name
        projects = jira_dgp[name]
        dgp_worklog_today = get_worklog_dgp.Get_Today_Logged_Work(person, projects)
        if person in summary:
            summary[person] += dgp_worklog_today[person]
        else:
            summary.update(dgp_worklog_today)

    for name in jira_altatec:
        person = name
        projects = jira_altatec[name]
        altatec_worklog_today = get_worklog_altatec.Get_Today_Logged_Work(person, projects)
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
        print ("Person: ", person)
        if summary[person] == 0:
            if person in config.emails:
                for item in config.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов, не забудь это сделать.".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов, не забудь это сделать.".format('а', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = "Не оставлено признаков присутствия, ты залогировал{} {} часов.".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = "Не оставлено признаков присутствия, ты залогировал{} {} часов.".format('а', summary[person])
                        print ("name: ", item['name']) 
                        break
                smtp_sender.SendMessage(text_to_send, config.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 0 and summary[person] <= 3):
            if person in config.emails:
                for item in config.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов по всем проектам.".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов по всем проектам.".format('а', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = "Че-то маловато насыпал{} - {} часов. А где еще? А если найду?".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = "Че-то маловато насыпал{} - {} часов. А где еще? А если найду?".format('а', summary[person])
                        print ("name: ", item['name']) 
                        break
                smtp_sender.SendMessage(text_to_send, config.emails[person], texttype)
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] < 8):
            if person in config.emails:
                for item in config.employee:
                    if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов по всем проектам.".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 0:
                        text_to_send = "Сегодня ты залогировал{} {} часов по всем проектам".format('а', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                        text_to_send = "Ты уже залогировал{} - {} часов. А можешь ли больше?".format('', summary[person])
                        print ("name: ", item['name'])
                        break
                    elif item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                        text_to_send = "Ты уже залогировал{} - {} часов. А можешь ли больше?".format('а', summary[person])
                        print ("name: ", item['name']) 
                        break
                smtp_sender.SendMessage(text_to_send, config.emails[person], texttype)
            else: print ("no email")
        elif summary[person] >= 8:
            if person in config.emails:
                    for item in config.employee:
                        if item['name'] == person and item['sex'] == 'm' and item['joke_level'] == 1:
                            text_to_send = "Ты славно поработал{}, приятель{}! {} часов - это сильно!".format('','', summary[person])
                            print ("Человек несмеющийся: ", item['name'])
                        if item['name'] == person and item['sex'] == 'w' and item['joke_level'] == 1:
                            text_to_send = "Ты славно поработал{}, приятель{}! {} часов - это сильно!".format('а', 'ница', summary[person])
                            print ("name: ", item['name'])
                    smtp_sender.SendMessage(text_to_send, config.emails[person], texttype)
            else: print ("no email")
    
    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, 'e.barnaev@altatec.ru', texttype)
