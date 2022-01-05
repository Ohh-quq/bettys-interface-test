import requests
import coo_setting

url="http://172.16.12.115:8080/#/act-exp/2/rosters?activityName=1"
#url="http://172.16.12.115:8080/v2/api-docs/activities/2/rosters/pages?page=0&size=10&enabled=true&sort=generateDate,desc"
headers={
    'Content-Type':'application/json;charset=UTF-8',
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDA4NTc3MTQsInVzZXJfbmFtZSI6ImFkbWluIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiJdLCJqdGkiOiI2NDY3YmU4Ni00ZGNjLTQxZjUtYmVjYS0yYmYwOGJkMGUyYWUiLCJjbGllbnRfaWQiOiJkZWZhdWx0Iiwic2NvcGUiOlsiYWxsIl19.OPc1AHfHT4pe3lPvqNu8XbRzwYyvFa_ZFFK3Ko_b0NqOlx2N2c3IIirBifhDKBJI1VsBiWZZ5djT3IsiPlVrX843p7RKbgs-u227ivvKe2AXLq_FY2ZwGYJtng0YpHabeFdZTi6q2AD9pgQB5aAATx6QDLkxB5hhkRmhQ4g6OleAfV-KW48XfYLumI_q0voMhL5EcwcYQ1vysS5_JiGFLgiIQQEAEQGJL0Cc8jbCSTO2hy8YcOqWYCW5m4SuVi8chEwUOlPQZbKd7pJ_wAQTNqVGnxZtdwk6zFpK812oIQC0oSjz2SAoKBjCJ59VfwvQCDUQfJ3Pr3KSpkQ_GVrCcw",
}

'''res=requests.get(url=url)
res=requests.get(url=url,headers=headers)
print(res.content.decode())'''

url1 = "http://172.16.12.115:8154/access/checkResourceAccess"
data = {
    "permission": "READ",
    "resourceId": 0,
    "resourceType": "TAG"
}
res2 = requests.post(url=url1, json=data, headers=headers)


print(res2)
print(res2.content.decode())
print(res2.status_code)

#print(res.content)
#print(res.text)
