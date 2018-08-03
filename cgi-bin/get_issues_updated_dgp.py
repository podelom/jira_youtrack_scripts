#!C:\Python36\python.exe
from jira import JIRA
import urllib3
urllib3.disable_warnings()

jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth^6'), options = {'server': 'https://dgpjira.alfakom.org/', 'verify':'cgi-bin/certs.pem'})
#jira = jira = JIRA(basic_auth=('e.barnaev', 'Rfqhfnrth^6'), options = {'server': 'https://dgpjira.alfakom.org/', 'verify':False})
def Get_Currnet_Month_Updated_Issues():
    base_request = 'updated >= startOfMonth() and project = BUS'
    all_proj_current_month = jira.search_issues(base_request)
    #print("\ncurrent month updated: ",all_proj_current_month)
    return(all_proj_current_month)

def Get_Previous_Month_Updated_Issues():
    base_request = 'updated >= startOfMonth(-1)  and updated <= startOfMonth() and project = BUS'
    all_proj_previous_month = jira.search_issues(base_request)
    #print("\nprevious month updated: ",all_proj_previous_month)
    return(all_proj_previous_month)

def Get_Today_Updated_Issues():
    base_request = 'updated >= startOfDay() and project = BUS'
    all_proj_today_updated = jira.search_issues(base_request)
#    print("\ntoday updated: ", all_proj_today_updated)
    return(all_proj_today_updated)

def Get_Yesterday_Updated_Issues():
    base_request = 'updated >= startOfDay(-1) and updated <= startOfDay() and project = BUS'
    all_proj_yesterday_updated = jira.search_issues(base_request)
#    print("\nyesterday updated: ",all_proj_yesterday_updated)
    return(all_proj_yesterday_updated)

#Get_Currnet_Month_Updated_Issues()
#Get_Previous_Month_Updated_Issues()
#Get_Today_Updated_Issues()
#Get_Yesterday_Updated_Issues()
