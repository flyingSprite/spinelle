import json
import requests

# Disable security request warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

""" Order 2: Login system by https

This is the code which use curl to login system
```
curl -k https://192.168.105.88/axapi/v3/auth -H "Content-type:application/json" -d '{
    "credentials": {
        "username": "admin", 
        "password": "a10"
    }
}'
```
"""


class LoginSystemByHttps(object):
    login_url = 'https://192.168.105.88/axapi/v3/auth'

    def login(self):
        """
        Note: the dict playload must be use json.dumps() to turn to str.
        :return: Result string data
        """
        payload = {'credentials': {'username': "admin", 'password': "a10"}}
        headers = {'content-type': 'application/json', 'Connection': 'keep-alive'}
        response = requests.post(self.login_url, data=json.dumps(payload), verify=False, headers=headers)
        print(response.text)
        return response.text


# Order 2 testing:
# login = LoginSystemByHttps()
# login.login()
