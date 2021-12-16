import requests
import json

username = 'Malphit'
katalog = 'repos'
response = requests.get(f'https://api.github.com/users/{username}/{katalog}')
response.json()

with open('lesson1.json','w') as f:
    json.dump(response.json(), f)

for i in response.json():
    print(i['name'])