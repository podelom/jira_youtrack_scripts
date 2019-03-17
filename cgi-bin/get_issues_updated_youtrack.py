#!/usr/local/bin/python3
import json
import requests
import securer_prod


api_token = securer_prod.youtrack_credentials['token']
ytrck_url = securer_prod.youtrack_credentials['link']

headers = {'Accept': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def Get_Currnet_Month_Updated_Issues(person, projects):
    base_request = '{}/rest/issue?filter=work+author%3A+{}+work+date%3A+%7BThis+month%7D+project%3A+{}'.format(ytrck_url, person, projects)
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
    base_request = '{}/rest/issue?filter=work+author%3A+{}+project%3A+{}+work+date%3A+%7BLast+month%7D'.format(ytrck_url, person, projects)
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
    base_request = '{}/rest/issue?filter=work+author%3A+{}+work+date%3A+Today+project%3A+{}'.format(ytrck_url, person, projects)
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
    base_request = '{}/rest/issue?filter=work+author%3A+{}+work+date%3A+Yesterday+project%3A+{}'.format(ytrck_url, person, projects)
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
