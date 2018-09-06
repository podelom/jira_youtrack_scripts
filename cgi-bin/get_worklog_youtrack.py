#!/usr/local/bin/python3
import json
import requests
import get_issues_updated_youtrack
import datetime
import time
from datetime import datetime, timedelta

api_token = 'perm:ZS5iYXJuYWV2.R2V0V29ya2xvZw==.AuVc0X3Df1iHyY6ljWBauvrKM7WPoi'
#api_url_base = 'http://vps580284.ovh.net:8081/rest/issue'
#api_url_base = 'http://vps580284.ovh.net:8081/rest/issue?filter=for%3A+e.barnaev+work+date%3A2018-07-01+..+2018-07-31'
api_url_base = 'http://vps580284.ovh.net:8081/rest/issue/TKP-1/timetracking/workitem/'
 #e.barnaev  work date: 2018-07-01 .. 2018-07-31
#GET http://localhost:8081/rest/issue?filter=for%3A+me+%23Unresolved+%23Exception&filter=for%3A+me+%23Unresolved+%23Show-stopper

headers = {'Accept': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def Convert_Minutes_To_Hours(str):
    hours = 0
    hours = int(str)/60
    rhours = round(hours, 3)
    #print("rhours: ", rhours)
    return(rhours)

def Yesterday_Date():
    today = datetime.now()
    date = datetime.date(today)
    yesterday = date - timedelta(days=1)
    return(yesterday)

def Today_Date():
    d = datetime.now()
    date = datetime.date(d)
    return(date)

def TimeStampToDate(timestamp):
    timstamp_to_time = time.strftime('%Y-%m-%d', time.localtime(timestamp/1000))
    time_to_datetime = datetime.strptime(timstamp_to_time, '%Y-%m-%d')
    date_check = datetime.date(time_to_datetime)
    return(date_check)

def Start_Of_The_Month_Date():
    d = datetime.now()
    date = datetime.date(d)
    first_day_month = date.replace(day=1)
    return(first_day_month)

def Start_Of_The_Previous_Month_Date():
    d = datetime.now()
    date = datetime.date(d)
    previuos_month = date.replace(month=date.month - 1)
    first_day_previous_month = previuos_month.replace(day=1)
    return(first_day_previous_month)

#TimeStampToDate()

def Get_Current_Month_Logged_Work(person, projects):
    person_with_hours = {person: 0}
    issues = get_issues_updated_youtrack.Get_Currnet_Month_Updated_Issues(person, projects)
    for issue in issues:
        link = 'http://vps580284.ovh.net:8081/rest/issue/{}/timetracking/workitem/'.format(issue)
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            for worklog in data:
                if TimeStampToDate(worklog['date']) >= Start_Of_The_Month_Date() and TimeStampToDate(worklog['date']) < Today_Date():
                    if person == worklog['author']['login']:
                        hours = Convert_Minutes_To_Hours(worklog['duration'])
                        person_with_hours[person] += hours
        else:
            return None
    print("person with hours Current Month: ", person_with_hours)
    return(person_with_hours)
def Get_Previous_Month_Logged_Work(person, projects):
    person_with_hours = {person: 0}
    issues = get_issues_updated_youtrack.Get_Previous_Month_Updated_Issues(person, projects)
    for issue in issues:
        link = 'http://vps580284.ovh.net:8081/rest/issue/{}/timetracking/workitem/'.format(issue)
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            for worklog in data:
                if TimeStampToDate(worklog['date']) >= Start_Of_The_Previous_Month_Date() and TimeStampToDate(worklog['date']) < Start_Of_The_Month_Date():
                    if person == worklog['author']['login']:
                        hours = Convert_Minutes_To_Hours(worklog['duration'])
                        person_with_hours[person] += hours
        else:
            return None
    print("person with hours Previuos Month: ", person_with_hours)
    return(person_with_hours)

def Get_Today_Logged_Work(person, projects):
    person_with_hours = {person: 0}
    issues = get_issues_updated_youtrack.Get_Today_Updated_Issues(person, projects)
    for issue in issues:
        link = 'http://vps580284.ovh.net:8081/rest/issue/{}/timetracking/workitem/'.format(issue)
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            for worklog in data:
                if TimeStampToDate(worklog['date']) == Today_Date():
                    if person == worklog['author']['login']:
                        hours = Convert_Minutes_To_Hours(worklog['duration'])
                        print("hours: ", hours)
                        person_with_hours[person] += hours
        else:
            return None
    print("person with hours Today: ", person_with_hours)
    return(person_with_hours)

def Get_Yesterday_Logged_Work(person, projects):
    person_with_hours = {person: 0}
    issues = get_issues_updated_youtrack.Get_Yesterday_Updated_Issues(person, projects)
    for issue in issues:
        link = 'http://vps580284.ovh.net:8081/rest/issue/{}/timetracking/workitem/'.format(issue)
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            for worklog in data:
                if TimeStampToDate(worklog['date']) == Yesterday_Date():
                    if person == worklog['author']['login']:
                        hours = Convert_Minutes_To_Hours(worklog['duration'])
                        print("hours: ", hours)
                        person_with_hours[person] += hours
        else:
            return None
    print("person with hours Yesterday: ", person_with_hours)
    return(person_with_hours)

#Get_Current_Month_Logged_Work('e.barnaev', 'TKP')
#Get_Previous_Month_Logged_Work('e.barnaev', 'TKP')
Get_Today_Logged_Work('e.barnaev', 'TKP')
#Get_Yesterday_Logged_Work('e.barnaev', 'TKP')


