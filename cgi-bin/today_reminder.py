#!/usr/local/bin/python3

import get_worklog_altatec
import get_worklog_dgp
import config
import smtp_sender
import json


if __name__ == "__main__":
    jira_dgp = config.jira_dgp
    jira_altatec = config.jira_altatec
    summary = {}
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

    for person in summary:
        print ("Person: ", person)
        if summary[person] == 0:
            text_to_send = "На текущий момент в сегодняшний день залогированно: {}. Настал час залогировать в свои проекты время потраченное!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 0 and summary[person] <= 3):
            text_to_send = "Я вижу что-то сделано: {}. Но явно не всё мне видно. Залогируй оставшееся время пожалуйста!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif (summary[person] > 3 and summary[person] <= 8):
            text_to_send = "Сделано не мало: {}. Не забудь залогировать оставшееся!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")
        elif summary[person] > 8:
            text_to_send = "Вот это результат: {}!. Отдохни старина, это был славный день!".format(summary[person])
            if person in config.emails:
                smtp_sender.SendMessage(text_to_send, config.emails[person])
            else: print ("no email")

    otchet = json.dumps(summary)
    smtp_sender.SendMessage(otchet, 'e.barnaev@altatec.ru')
