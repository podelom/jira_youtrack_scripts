#!/usr/local/bin/python3
##!C:\Python36\python.exe
from jira import JIRA
import urllib3
urllib3.disable_warnings()

#jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth#3'), options = {'server': 'https://jira.i.altatec.ru', 'verify':'jira_altatec.pem'})
jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth@2Mm'), options = {'server': 'https://jira.i.altatec.ru', 'verify':False})
def Get_Currnet_Month_Updated_Issues(person, projects):
    projects_list = ", ".join(projects)
    base_request = "worklogDate >= startOfMonth() and project in ({}) and worklogAuthor = {}".format(projects_list, person)
    all_proj_current_month = jira.search_issues(base_request)
    #print("\ncurrent month updated: ",all_proj_current_month)
    return(all_proj_current_month)

def Get_Previous_Month_Updated_Issues(person, projects):
    projects_list = ", ".join(projects)
    base_request = "worklogDate <= startOfMonth() and worklogDate >= startOfMonth(-1) and project in ({}) and worklogAuthor = {}".format(projects_list, person)
    all_proj_previous_month = jira.search_issues(base_request)
    #print("\nprevious month updated: ",all_proj_previous_month)
    return(all_proj_previous_month)

def Get_Today_Updated_Issues(person, projects):
    projects_list = ", ".join(projects)
    base_request = "worklogDate >= startOfDay() and project in ({}) and worklogAuthor = {}".format(projects_list, person)
    all_proj_today_updated = jira.search_issues(base_request)
#    print("\ntoday updated: ", all_proj_today_updated)
    return(all_proj_today_updated)

def Get_Yesterday_Updated_Issues(person, projects):
    projects_list = ", ".join(projects)
    base_request = "worklogDate >= startOfDay(-1) and worklogDate <= startOfDay() and project in ({}) and worklogAuthor = {}".format(projects_list, person)
    all_proj_yesterday_updated = jira.search_issues(base_request)
#    print("\nyesterday updated: ",all_proj_yesterday_updated)
    return(all_proj_yesterday_updated)

#Get_Currnet_Month_Updated_Issues('e.barnaev', ['dgpbus', 'rotek', 'rustek'])
#Get_Previous_Month_Updated_Issues('e.barnaev', ['dgpbus', 'rotek', 'rustek'])
#Get_Today_Updated_Issues()
#Get_Yesterday_Updated_Issues()
