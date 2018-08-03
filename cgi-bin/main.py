#!/usr/local/bin/python3


##!C:\Python36\python.exe
import get_worklog_altatec
import get_worklog_dgp
#import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt, mpld3
#import jinja2

# plotly token aniu3e4fp3
if __name__ == "__main__":
    #DGP logs
    dgp_worklog_current_month = get_worklog_dgp.Get_Current_Month_Logged_Work()
    dgp_worklog_today = get_worklog_dgp.Get_Today_Logged_Work()
    dgp_worklog_yesterday = get_worklog_dgp.Get_Yesterday_Logged_Work()
    #ALTATEC worklog
    altatec_worklog_current_month = get_worklog_altatec.Get_Current_Month_Logged_Work()


    pattern_head = '''
    <!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Wall</title>
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
    print("<div><br>", "DGP WORKLOG today")
    for value in dgp_worklog_today:
        print ("<div>", value, " = ", dgp_worklog_today[value], "<br>")
    print("<div><br>", "DGP WORKLOG yesterday")
    for value in dgp_worklog_yesterday:
        print ("<div>", value, " = ", dgp_worklog_yesterday[value], "<br>")
    print("<div><br>", "ALtatec WORKLOG current month")
    for value in altatec_worklog_current_month:
        print ("<div>", value, " = ", altatec_worklog_current_month[value], "<br>")

    print(pattern_bottom)
#    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
#    mpld3.show()

    #plt.fig_to_html()
