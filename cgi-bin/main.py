#!/usr/local/bin/python3

import get_worklog_altatec
import get_worklog_dgp
import config


# plotly token aniu3e4fp3
if __name__ == "__main__":
    #DGP logs
    jira_dgp = config.jira_dgp
    jira_altatec = config.jira_altatec
    dgp_worklog_current_month = {}
    dgp_worklog_previous_month = {}
    dgp_worklog_yesterday = {}
    dgp_worklog_today = {}
    altatec_worklog_current_month = {}
    altatec_worklog_previous_month = {}
    altatec_worklog_yesterday = {}
    altatec_worklog_today = {}

    summary_dgp = {}

    for name in jira_altatec:
        person = name
        print ("name", name)
        projects = jira_altatec[name]
        print ("projects", projects)
        worklog_current_month = get_worklog_altatec.Get_Current_Month_Logged_Work(person, projects)
        print ("altatec_worklog_current_month", worklog_current_month)
        altatec_worklog_current_month.update(worklog_current_month)

        worklog_previous_month = get_worklog_altatec.Get_Previous_Month_Logged_Work(person, projects)
        print ("altatec_worklog_previous_month", worklog_previous_month)
        altatec_worklog_previous_month.update(worklog_previous_month)

        worklog_yesterday = get_worklog_altatec.Get_Yesterday_Logged_Work(person, projects)
        print ("altatec_worklog_yesterday", worklog_yesterday)
        altatec_worklog_yesterday.update(worklog_yesterday)

        worklog_today = get_worklog_altatec.Get_Today_Logged_Work(person, projects)
        print ("altatec_worklog_today", worklog_today)
        altatec_worklog_today.update(worklog_today)

    for name in jira_dgp:
        person = name
        print ("name", name)
        projects = jira_dgp[name]
        print ("projects", projects)
        worklog_current_month = get_worklog_dgp.Get_Current_Month_Logged_Work(person, projects)
        print ("dgp_worklog_current_month", worklog_current_month)
        dgp_worklog_current_month.update(worklog_current_month)

        worklog_previous_month = get_worklog_dgp.Get_Previous_Month_Logged_Work(person, projects)
        print ("dgp_worklog_previous_month", worklog_previous_month)
        dgp_worklog_previous_month.update(worklog_previous_month)

        worklog_yesterday = get_worklog_dgp.Get_Yesterday_Logged_Work(person, projects)
        print ("dgp_worklog_yesterday", worklog_yesterday)
        dgp_worklog_yesterday.update(worklog_yesterday)

        worklog_today = get_worklog_dgp.Get_Today_Logged_Work(person, projects)
        print ("dgp_worklog_today", worklog_today)
        dgp_worklog_today.update(worklog_today)
    #dgp_worklog_current_month = get_worklog_dgp.Get_Current_Month_Logged_Work()
    #dgp_worklog_today = get_worklog_dgp.Get_Today_Logged_Work()
    #dgp_worklog_yesterday = get_worklog_dgp.Get_Yesterday_Logged_Work()
    #ALTATEC worklog
    #altatec_worklog_current_month = get_worklog_altatec.Get_Current_Month_Logged_Work()


    pattern_head = '''
    <!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Wall</title>
    <link rel="icon" type="image/png" href="favicon.ico">
    </head>
    <body>
    '''


    pattern_bottom = '''
    </body>
    </html>
    '''
    print('Content-type: text/html\n')
    print(pattern_head)

    print("<div><br>", "DGP WORKLOG current month")
    for value in dgp_worklog_current_month:
        print ("<div>", value, " = ", dgp_worklog_current_month[value], "<br>")
    print("<div><br>", "DGP WORKLOG previuos month")
    for value in dgp_worklog_previous_month:
        print ("<div>", value, " = ", dgp_worklog_previous_month[value], "<br>")
    print("<div><br>", "DGP WORKLOG yesterday")
    for value in dgp_worklog_yesterday:
        print ("<div>", value, " = ", dgp_worklog_yesterday[value], "<br>")
    print("<div><br>", "DGP WORKLOG today")
    for value in dgp_worklog_today:
        print ("<div>", value, " = ", dgp_worklog_today[value], "<br>")

    print("<div><br>", "ALtatec WORKLOG current month")
    for value in altatec_worklog_current_month:
        print ("<div>", value, " = ", altatec_worklog_current_month[value], "<br>")
    print("<div><br>", "ALtatec WORKLOG previuos month")
    for value in altatec_worklog_previous_month:
        print ("<div>", value, " = ", altatec_worklog_previous_month[value], "<br>")
    print("<div><br>", "ALtatec WORKLOG yesterday")
    for value in altatec_worklog_yesterday:
        print ("<div>", value, " = ", altatec_worklog_yesterday[value], "<br>")
    print("<div><br>", "ALtatec WORKLOG today")
    for value in altatec_worklog_today:
        print ("<div>", value, " = ", altatec_worklog_today[value], "<br>")


    print(pattern_bottom)
#    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
#    mpld3.show()

    #plt.fig_to_html()
