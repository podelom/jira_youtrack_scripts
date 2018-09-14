#!/usr/bin/python3

import get_worklog_altatec
import get_worklog_dgp
import get_worklog_youtrack
import config
import smtp_sender
import json


if __name__ == "__main__":
    jira_dgp = config.jira_dgp
    jira_altatec = config.jira_altatec
    youtrack_tkp = config.youtrack_tkp
    summary = {}
    for name in jira_dgp:
        person = name
        projects = jira_dgp[name]
        dgp_worklog_today = get_worklog_dgp.Get_Yesterday_Logged_Work(person, projects)
        if person in summary:
            summary[person] += dgp_worklog_today[person]
        else:
            summary.update(dgp_worklog_today)

    for name in jira_altatec:
        person = name
        projects = jira_altatec[name]
        altatec_worklog_today = get_worklog_altatec.Get_Yesterday_Logged_Work(person, projects)
        if person in summary:
            summary[person] += altatec_worklog_today[person]
        else:
            summary.update(altatec_worklog_today)

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

    for person in summary:
        print ("Person: ", person)
        if summary[person] == 0:
            if person in config.emails:
                for name in config.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('а', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = "Не оставлено признаков присутствия, ты залогтилвал{} {} часов вчера.".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = "Не оставлено признаков присутствия, ты залогтилвал{} {} часов вчера.".format('а', summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: print ("no employee")
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 0 and summary[person] <= 3):
            if person in config.emails:
                for name in config.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('а', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = "Че-то маловато насыпал{} - {} часов вчера. А где еще? А если найду?".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = "Че-то маловато насыпал{} - {} часов вчера. А где еще? А если найду?".format('а', summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: print ("no employee")
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] < 8):
            if person in config.emails:
                for name in config.employee:
                    if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 0:
                        text_to_send = "Вчера ты залогировал{} {} часов, сегодня не забудь.".format('а', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                        text_to_send = "Вчера ты залогировал{} - {} часов. А можешь больше?".format('', summary[person])
                        print ("name: ", name['name'])
                        break
                    elif name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                        text_to_send = "Вчера ты залогировал{} - {} часов. А можешь больше?".format('а', summary[person])
                        print ("name: ", name['name']) 
                        break
                    else: print ("no employee")
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif summary[person] >= 8:
            if person in config.emails:
                    for name in config.employee:
                        if name['name'] == person and name['sex'] == 'm' and name['joke_level'] == 1:
                            text_to_send = "А ты вчера упорол{}, приятель{}! {} часов - это сильно!".format('ся','', summary[person])
                        if name['name'] == person and name['sex'] == 'w' and name['joke_level'] == 1:
                            text_to_send = "А ты вчера упорол{}, приятель{}! {} часов - это сильно!".format('ась', 'ница', summary[person])
                            print ("name: ", name['name'])
                        else: print ("no employee")
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")

    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, 'e.barnaev@altatec.ru')
