import requests

contenu=requests.get("http://api.open-notify.org/astros.json")

liste_contenu=list()
for ligne in contenu:
    liste_contenu.append(ligne)
