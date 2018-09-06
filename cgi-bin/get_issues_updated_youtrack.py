#!/usr/local/bin/python3
import json
import requests


api_token = 'perm:ZS5iYXJuYWV2.R2V0V29ya2xvZw==.AuVc0X3Df1iHyY6ljWBauvrKM7WPoi'
#api_url_base = 'http://vps580284.ovh.net:8081/rest/issue'
api_url_base_this_month = 'http://vps580284.ovh.net:8081/rest/issue?filter=for%3A+e.barnaev+work+date%3A+%7BThis+month%7B+project%3A+TKP'
api_url_base_last_month = 'http://vps580284.ovh.net:8081/rest/issue?filter=for%3A+e.barnaev+work+date%3A+%7BLast+month%7B+project%3A+TKP'
api_url_base_today = 'http://vps580284.ovh.net:8081/rest/issue?filter=for%3A+e.barnaev+work+date%3A+Today+project%3A+TKP'
api_url_base_yesterday = 'http://vps580284.ovh.net:8081/rest/issue?filter=for%3A+e.barnaev+work+date%3A+Yesterday+project%3A+TKP'
#api_url_base = 'http://vps580284.ovh.net:8081/rest/issue/TKP-1/timetracking/workitem/'
 #e.barnaev  work date: 2018-07-01 .. 2018-07-31
#GET http://localhost:8081/rest/issue?filter=for%3A+me+%23Unresolved+%23Exception&filter=for%3A+me+%23Unresolved+%23Show-stopper

headers = {'Accept': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def Get_Currnet_Month_Updated_Issues(person, projects):
    base_request = 'http://vps580284.ovh.net:8081/rest/issue?filter=work+author%3A+{}+work+date%3A+%7BThis+month%7D+project%3A+{}'.format(person, projects)
    issues_with_worklog = []
    api_url = '{0}'.format(base_request)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        for content in data:
            issue = data[content]
            for a in issue:
            #    print ("issue current month: ", a['id'])
                issues_with_worklog.append(a['id'])
    return(issues_with_worklog)

def Get_Previous_Month_Updated_Issues(person, projects):
    base_request = 'http://vps580284.ovh.net:8081/rest/issue?filter=work+author%3A+{}+project%3A+{}+work+date%3A+%7BLast+month%7D'.format(person, projects)
    issues_with_worklog = []
    api_url = '{0}'.format(base_request)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        for content in data:
            issue = data[content]
            for a in issue:
              #  print ("issue prev month: ", a['id'])
                issues_with_worklog.append(a['id'])
    return(issues_with_worklog)

def Get_Today_Updated_Issues(person, projects):
    base_request = 'http://vps580284.ovh.net:8081/rest/issue?filter=work+author%3A+{}+work+date%3A+Today+project%3A+{}'.format(person, projects)
    issues_with_worklog = []
    api_url = '{0}'.format(base_request)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        for content in data:
            issue = data[content]
            for a in issue:
              #  print ("issue Today: ", a['id'])
                issues_with_worklog.append(a['id'])
    return(issues_with_worklog)

def Get_Yesterday_Updated_Issues(person, projects):
    base_request = 'http://vps580284.ovh.net:8081/rest/issue?filter=work+author%3A+{}+work+date%3A+Yesterday+project%3A+{}'.format(person, projects)
    issues_with_worklog = []
    api_url = '{0}'.format(base_request)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        for content in data:
            issue = data[content]
            for a in issue:
               # print ("issue Yesterday: ", a['id'])
                issues_with_worklog.append(a['id'])
    return(issues_with_worklog)

Get_Currnet_Month_Updated_Issues('e.barnaev', 'TKP')
Get_Previous_Month_Updated_Issues('e.barnaev', 'TKP')
Get_Today_Updated_Issues('e.barnaev', 'TKP')
Get_Yesterday_Updated_Issues('e.barnaev', 'TKP')
