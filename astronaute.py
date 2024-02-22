# Templier Timothée

import requests

contenu=requests.get("http://api.open-notify.org/astros.json")

for i in contenu.json()["people"]:
    if i['craft'] == 'ISS':
        print(i['name'])