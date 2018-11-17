
import requests
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'username': "root",
           'password': "root"}

ret = requests.post("127.0.0.1:8000/api-token-auth/", headers=headers, data=json.dumps(payload))
print(ret)

print('ok')

