#!C:\Python36\python.exe
from jira import JIRA, JIRAError
import get_issues_updated_dgp
from datetime import datetime, timedelta
import urllib3


jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth^6'), options = {'server': 'https://dgpjira.alfakom.org/', 'verify':'cgi-bin/certs.pem'})
#jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth^6'), options = {'server': 'https://dgpjira.alfakom.org/', 'verify':False})


epmployees_worklog_today = {'e.barnaev': 0, 'e.zelenov': 0, 'm.orischenko': 0, 'p.pupkin': 0}
epmployees_worklog_yesterday = {'e.barnaev': 0, 'e.zelenov': 0, 'm.orischenko': 0, 'p.pupkin': 0}
epmployees_worklog_current_month = {'a.sheviakov': 0, 'e.barnaev': 0, 'e.zelenov': 0, 'm.orischenko': 0, 'e.belousov': 0, 'p.pupkin': 0, 'a.makushev': 0, 'v.sapunov': 0, 'e.ostretsov': 0, 'y.chernov': 0}
epmployees_worklog_previous_month = {'e.barnaev': 0, 'e.zelenov': 0, 'm.orischenko': 0, 'p.pupkin': 0}
fullnames = {}

urllib3.disable_warnings()
def Convert_Seconds_To_Hours(str):
    hours = 0
    hours = int(str)/3600
    rhours = round(hours, 3)
    #print("rhours: ", rhours)
    return(rhours)

def Worklog_Date(d):
    source_date = d[0:10]  # - timedelta(days=days_to_subtract)
    convert_string_to_date = datetime.strptime(source_date, '%Y-%m-%d')
    date = datetime.date(convert_string_to_date)
    return(date)

def Today_Date():
    d = datetime.now()
    date = datetime.date(d)
    return(date)

def Yesterday_Date():
    today = datetime.now()
    date = datetime.date(today)
    yesterday = date - timedelta(days=1)
    return(yesterday)

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

def Get_Today_Logged_Work():
    for issue in get_issues_updated_dgp.Get_Today_Updated_Issues():
        try:
            for item in jira.worklogs(issue):
                worklog = jira.worklog(issue, item)
                if Worklog_Date(worklog.started) == Today_Date():
                    if worklog.author.name in epmployees_worklog_today:
                        for employee in epmployees_worklog_today:
                            if  worklog.author.name == employee:
                                hours = Convert_Seconds_To_Hours(worklog.timeSpentSeconds)
                                epmployees_worklog_today[worklog.author.name] += hours
        except JIRAError as e:
            print("FUCK OFF: ", e.status_code, e.text)
            continue
    #        print ("id: ", issue.id)
    #        print ("key: ", issue.key)
#    print("epmployees_worklog_today: ", epmployees_worklog_today)
    return(epmployees_worklog_today)

def Get_Yesterday_Logged_Work():
    for issue in get_issues_updated_dgp.Get_Currnet_Month_Updated_Issues():
        try:
            for item in jira.worklogs(issue):
                worklog = jira.worklog(issue, item)
                if Worklog_Date(worklog.started) == Yesterday_Date():
                    if worklog.author.name in epmployees_worklog_yesterday:
                        for employee in epmployees_worklog_yesterday:
                            if  worklog.author.name == employee:
                                hours = Convert_Seconds_To_Hours(worklog.timeSpentSeconds)
                                epmployees_worklog_yesterday[worklog.author.name] += hours
        except JIRAError as e:
            print("FUCK OFF: ", e.status_code, e.text)
            continue
#    print("epmployees_worklog_yesterday: ", epmployees_worklog_yesterday)
    return(epmployees_worklog_yesterday)

def Get_Current_Month_Logged_Work():
    for issue in get_issues_updated_dgp.Get_Currnet_Month_Updated_Issues():
        try:
            for item in jira.worklogs(issue):
                worklog = jira.worklog(issue, item)
                if Worklog_Date(worklog.started) >= Start_Of_The_Month_Date() and Worklog_Date(worklog.started) <= Today_Date():
                    if worklog.author.name in epmployees_worklog_current_month:
                        for employee in epmployees_worklog_current_month:
                            if  worklog.author.name == employee:
                                hours = Convert_Seconds_To_Hours(worklog.timeSpentSeconds)
                                epmployees_worklog_current_month[worklog.author.name] += hours
        except JIRAError as e:
            print("FUCK OFF: ", e.status_code, e.text)
            continue
#    print("epmployees_worklog_current_month: ", epmployees_worklog_current_month)
    return(epmployees_worklog_current_month)

def Get_Start_Of_The_Previous_Month_Date():
    for issue in get_issues_updated_dgp.Get_Previous_Month_Updated_Issues():
        try:
            for item in jira.worklogs(issue):
                worklog = jira.worklog(issue, item)
                if Worklog_Date(worklog.started) >= Start_Of_The_Previous_Month_Date() and Worklog_Date(worklog.started) < Start_Of_The_Month_Date():
                    if worklog.author.name in epmployees_worklog_previous_month:
                        for employee in epmployees_worklog_previous_month:
                            if  worklog.author.name == employee:
                                hours = Convert_Seconds_To_Hours(worklog.timeSpentSeconds)
                                epmployees_worklog_previous_month[worklog.author.name] += hours
        except JIRAError as e:
            print("FUCK OFF: ", e.status_code, e.text)
            continue
    print ("key: ", issue.key)
#    print("epmployees_worklog_previous_month: ", epmployees_worklog_previous_month)
    return(epmployees_worklog_previous_month)


#Get_Today_Logged_Work()
#Get_Yesterday_Logged_Work()
#Get_Current_Month_Logged_Work()
#Get_Start_Of_The_Previous_Month_Date()
