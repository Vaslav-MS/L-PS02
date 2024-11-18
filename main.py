import requests
import pprint

# 1 ЗАДАНИЕ

params = {
    'q': 'html'
}
response = requests.get(url = 'https://api.github.com/search/repositories', params = params)
response_json = response.json()
print(response.status_code) # статус-код ответа
pprint.pprint(response_json) # json

# 2 ЗАДАНИЕ

params = {
    'userId': 1
}
response = requests.get(url = 'https://jsonplaceholder.typicode.com/posts', params = params)
print(response.text)

# 3 ЗАДАНИЕ

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "title": "extern",
    "body": "konkistance 2 konkistance",
    "userId": 35
}

response = requests.post(url=url, data=data)
print(response.status_code)
print(response.text)