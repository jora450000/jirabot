#!/bin/python3

from jira import JIRA
import re
import requests
import datetime

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
jira = JIRA(server="https://jira.domain.local", basic_auth=('login', 'password'),validate=False,)

project_key = "ITOSA"

today = datetime.datetime.now() - datetime.timedelta(days=3)

jql = f"project = {project_key}  AND  worklogDate >= \"{today.year}/{today.month}/{today.day}\" AND status = \"Новый\""
issues_list = jira.search_issues(jql) 

for issue in issues_list:
#    print (issue.fields.project.key)             # 'JRA'
    print (issue.fields.customfield_10006)       # number of task
    print (issue.fields.issuetype.name)          # type of task
    print (issue.fields.reporter.displayName)    # author
    print (issue.fields.status)
    
    yy = int(issue.fields.customfield_10202[0:4])  #my custom fields - see in Python IDE 
    mm = int(issue.fields.customfield_10202[5:7])
    dd = int(issue.fields.customfield_10202[8:10])
    hh = int(issue.fields.customfield_10202[11:13])
    mmin = int(issue.fields.customfield_10202[14:16])

    if datetime.datetime(yy,mm,dd, hh, mmin, 59) < datetime.datetime.now():
        print(f"{dd}.{mm}.{yy}  fake up")  



#    print (issue.fields.customfield_10202.)

#print(issues_list)







