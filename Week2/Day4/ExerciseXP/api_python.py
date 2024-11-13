import json
import requests

import os 
response = requests.get('https://api.chucknorris.io/jokes/random')
data = json.loads(response.text)
print(data)

dir_path = os.path.dirname(os.path.realpath(__file__))


with open('chuck_norris_jokes.json', 'a+') as file:
    json.dump(data, file, indent = 2, sort_keys=True)