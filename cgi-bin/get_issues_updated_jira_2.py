#!/usr/local/bin/python3

from jira import JIRA
import urllib3
import securer_templates
urllib3.disable_warnings()

jira_auth = securer_templates.jira_credentials_1
jira = jira = JIRA(basic_auth=(jira_auth['login'], jira_auth['password']), options = {'server': jira_auth['link'], 'verify':'certs.pem'})

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

#Get_Currnet_Month_Updated_Issues()
#Get_Previous_Month_Updated_Issues()
#Get_Today_Updated_Issues()
#Get_Yesterday_Updated_Issues()
