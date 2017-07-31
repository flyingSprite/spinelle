import json
import requests

""" Order 2: Login system by https

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
    login_url = 'http://192.168.105.88/axapi/v3/auth'

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


# login = LoginSystemByHttps()
# login.login()
