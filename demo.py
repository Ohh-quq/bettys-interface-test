import requests

import allocate_method
import coo_setting

url="http://172.16.12.115:8080/#/act-exp/2/rosters?activityName=1"
#url="http://172.16.12.115:8080/v2/api-docs/activities/2/rosters/pages?page=0&size=10&enabled=true&sort=generateDate,desc"
headers={
    'Content-Type':'application/json;charset=UTF-8',
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDEzNzczOTcsInVzZXJfbmFtZSI6ImFkbWluIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiJdLCJqdGkiOiJjYTIxZTc3MS01NGQzLTRkYjgtYjExYS05MjI0NDM3MDRiZjYiLCJjbGllbnRfaWQiOiJkZWZhdWx0Iiwic2NvcGUiOlsiYWxsIl19.rcVO6267yMYEjnPlxdW-VdQoPksa1l10ltaMmhECX7ukql0V22gRfrzYjNwR9CdxGmbIUH0wEA4x82M_z5u2tBlnjwwE5EhTetEKv8qYxly2i5_jaXXZKwHq1ekWqNAaiwLxtQuIUgVq1V6pBLHUrM0oYy06c9pmxdLNXRek5IG3eRETCx1xqbMcd8T_SwYQ0Ole57MSEhK1Yb8HataacnxttZa0yie4n5RzX_46IFGHyqF3RkJHuu53wUw7Mik3d6BoFkJedv0id2HS78ndybNahYgShYO5dx58zFngoQapRsUglKjE6UebVJm2TbtcKYwXodXM-hmSrAhg288s4w"}

'''res=requests.get(url=url)
res=requests.get(url=url,headers=headers)
print(res.content.decode())'''

# url1 = "http://172.16.12.115:8154/access/checkResourceAccess"
# data = {
#     "permission": "READ",
#     "resourceId": 0,
#     "resourceType": "TAG"
# }
# res2 = requests.post(url=url1, json=data, headers=headers)

url3 = "http://172.16.12.115:8154"
print(allocate_method.getpath(allocate_method.get_list[1]))
params = {
    "indicator":5
}
res3 = requests.get(url=url3, headers=headers)


print(res3)
print(res3.content.decode())
print(res3.status_code)

#print(res.content)
#print(res.text)
