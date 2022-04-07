import string 

data_input = list(string.ascii_letters + string.digits + "-")

def payload():
  print('yes')
  for char in data_input:
    sql = f"UNION SELECT 1,2 WHERE DATABASE like \"{char}%\"" 
    print(sql)

def testSQL():
  data = []
  payload()

def main():
  testSQL()

main()
