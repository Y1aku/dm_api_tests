import requests
import pprint

# Регистрация нового пользователя
'''
url = 'http://5.63.153.31:5051/v1/account'

headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
}

json_data = {
    'login': 'arbuzz7',
    'email': 'arbuzz7@mail.ru',
    'password': '123456789',
}

response = requests.post(url=url, headers=headers, json=json_data)
print(response.status_code)
pprint.pprint(response.json())
'''

# Активация зарегистрированного пользователя
headers = {
    'accept': 'text/plain',
}

response = requests.put('http://5.63.153.31:5051/v1/account/c9a53d2c-dd28-45d5-a45b-4900bdb89ad4', headers=headers)
print(response.status_code)
pprint.pprint(response.json())
response_json = response.json()
print(response_json['resource']['rating']['quantity'])

# Почта
'''
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
}

params = {
    'limit': '50',
}

response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, headers=headers, verify=False)
'''
