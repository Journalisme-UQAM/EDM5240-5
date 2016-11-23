# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.pc.gc.ca/apps/pdc/index_F.asp?oqYEAR=2016-2017&oqQUARTER=2"
fichier = "parcs-canada-JHR.csv"

entetes = {
    "User-Agent":"Peneloppe Tancrede - Requete envoyee dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
    "From":"tancredepeneloppe@gmail.com"
} 

contenu = requests.get(url,headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")

i = 0

for ligne in page.find_all("tr"):
    
    if i > 0:
        lien = ligne.a.get("href")
        hyperlien = "http://www.pc.gc.ca/apps/pdc/" + lien
        # print(hyperlien)

        contenu2 = requests.get(hyperlien,headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")
        # print(page2)
        
        contrat = []
        contrat.append(hyperlien)

        # for item in page2.find_all("tr"): # Ici, ça ne fonctionne pas, parce que dans le site que tu as choisi, les cellules des tableaux sont marquées par des éléments <div> et non <td>
        for item in page2.find_all("div", class_="divRightCol"): # Voici la syntaxe qu'il faudrait utiliser dans le cas du site de Parcs Canada
            print(item.text.strip())
            contrat.append(item.text.strip())
        print(contrat)
        
        fin = open(fichier,"a")
        projet = csv.writer(fin)
        projet.writerow(contrat)

# Dans un des scripts que je vous ai envoyés, j'ai fait une erreur.
# Quand on écrit « =+1 », on dit «la variable est égale à (plus) 1».
# C'est « +=1 » qu'il faut écrire pour augmenter de 1 la valeur d'une variable dans une boucle.
    # i =+ 1
    i += 1