#!/usr/local/bin/python3

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
        if summary[person] >= 0 and summary[person] <= 1:
            text_to_send = "За вчерашний день залогированных часов: {}. Что, совсем ничего не было?".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 1 and summary[person] <= 3):
            text_to_send = "Вчера немного залоггировано: {}. Но явно не всё мне видно. Залогируй оставшееся время пожалуйста!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] <= 8):
            text_to_send = "Сделано вчера немало: {}. Не забудь залогировать оставшееся!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif summary[person] > 8:
            text_to_send = "Вот это результат! {}!. Сегодня тоже не забудь :)".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")

    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, 'e.barnaev@altatec.ru')
