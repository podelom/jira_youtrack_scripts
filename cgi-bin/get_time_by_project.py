#!/usr/bin/python3

import get_worklog_altatec



jira_altatec = {'e.barnaev': ['dgpbus', 'rotek', 'rustek'],
        	 	'e.zelenov': ['dgpbus', 'DEPTRANS-RFID', 'DGPRFID', 'WH', 'VIDEOAA', 'KAMI', 'FTS', 'DOC', 'RFIDCS', 'DRFID' ]
        	   }

prj = {}
for name in jira_altatec:
	print ("name: ", name)
	projects = [0]
	for project in jira_altatec[name]:
		projects[0] = project
		wokrlog_today = get_worklog_altatec.Get_Today_Logged_Work(name, projects)
		prj[project] = wokrlog_today[name]
	print ("prj", prj)