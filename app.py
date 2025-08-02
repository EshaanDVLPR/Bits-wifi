import requests
import time

url = 'https://campnet.bits-goa.ac.in:8090/login.xml'

with open('info.txt') as f:
    text = f.read().split(",")
    # print(text)
    uname, pswd = text[0],text[1]

cur = str(time.time()).replace(".","")[:-3]
# print(cur,time.time())

data = {
'mode':191,
'username':uname,
'password':pswd,
'a':cur,
'producttype':0
}

head = {
    "Content-Type":"application/x-www-form-urlencoded",
    "host":"campnet.bits-goa.ac.in:8090",
    "origin":"https://campnet.bits-goa.ac.in:8090",
    "referer":"https://campnet.bits-goa.ac.in:8090/"
}

# print(requests.get('https://campnet.bits-goa.ac.in:8090/login.xml').headers)

requests.post(url=url,data=data,headers=head)