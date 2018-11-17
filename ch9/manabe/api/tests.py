
import requests
import json

'''
headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'username': "ccc",
           'password': "ccc"}
ret = requests.get("http://127.0.0.1:8000/api/users/?format=json", headers=headers)
print(ret.content)


mytoken = "f1365072e8bcf884ab9ce9158eb42d53e8fc0368"
url = "http://127.0.0.1:8000/api/servers/"
headers = {'Content-Type': 'application/json;charset=utf-8', 'Authorization': 'Token {}'.format(mytoken)}
payload = {'name': "192.168.1.212_8888",
           'ip_address': "192.168.1.212",
           'port': "8888",
           'salt_name': "192.168.1.212_8888",
           'app_name': "ZEP-BACKEND-NODEJS",
           'env_name': "TEST",
           'app_user': "root"
           }

ret = requests.post(url, headers=headers, data=json.dumps(payload))
print(str(ret.content, 'utf-8'))
print('ok')
'''

mytoken = "f1365072e8bcf884ab9ce9158eb42d53e8fc0368"
url = "http://127.0.0.1:8000/api/servers/811/"
headers = {'Content-Type': 'application/json;charset=utf-8', 'Authorization': 'Token {}'.format(mytoken)}
payload = {'name': "192.168.1.212_8888",
           'ip_address': "192.168.1.212",
           'port': "8888",
           'salt_name': "192.168.1.212_8888",
           'app_name': "ZEP-BACKEND-NODEJS",
           'env_name': "PRD",
           'app_user': "dvpusr"
           }

ret = requests.put(url, headers=headers, data=json.dumps(payload))
print(str(ret.content, 'utf-8'))
print('ok')



