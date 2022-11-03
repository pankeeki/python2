import json
import requests

vitsi = requests.get('https://api.chucknorris.io/jokes/random')
jooh = json.loads(vitsi.text)

print(jooh["value"])