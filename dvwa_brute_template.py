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
    pass
    
def testPasswords():
    pass
    
def createSession(payload,security=security,url=url,cookies=cookies):
    pass

    
testPasswords()
