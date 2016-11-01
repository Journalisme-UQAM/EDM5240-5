# coding: utf-8
# Comme nous avons appris à "coder" par le biais de Cloud9 et que nous utiliserons BS,
# j'ai initialement créé un environnement virtuel avec vos petits codes d'espions (virtualenv -p...), puis je l'ai ensuite activé.
# La communauté web étant ce qu'elle est, je comprends l'importance du travail collectif des développeurs...
# et je saisis également que Python ne peut pas tout faire. Qu'il faut parfois y ajouter des fonctionnalités externes.
# Cependant, je n'aurais pas su comment, ni quoi, importer en guise de modules externes sans vos notes (requests & BS4).

import csv
import requests
from bs4 import BeautifulSoup

# Pour commencer, après avoir importé les modules, il faut créer une variable avec l'URL où se trouve notre tableau de données.

url = "http://www.pc.gc.ca/apps/pdc/index_F.asp?oqYEAR=2016-2017&oqQUARTER=2"

# Je peux ensuite donner un nom à mon futur fichier csv (dans lequel sera confiner les résultats de ma moisson).

fichier = "parcs-canada.csv"

# Puisque les journalistes sont d'honorables sympathiques à l'éthique sans faille, 
# nous devons ensuite composer une entête qui sera envoyée au moment de notre requête afin de nous identifier.  

entetes = {
    "User-Agent":"Peneloppe Tancrede - Requete envoyee dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
    "From":"tancredepeneloppe@gmail.com"
} 

# Il faut ensuite demander à requests (importé précédemment) d'établir une connexion avec notre URL.
# Nous lui demanderons aussi de placer le contenu de celle-ci dans une variable éponyme. 

contenu = requests.get(url,headers=entetes)

# En guise d'essaie, nous pouvons envoyer notre requête afin de nous assurer que la réponse ne sera pas 404.

# print(contenu)

# Par la suite, nous demandons à BS de prendre le texte placé dans la variable contenu 
# et de l'analyse (le "parser").
# Le résultat de cette analyse se trouvera dans une variable supplémentaire, qu'on appelera page. 

page = BeautifulSoup(contenu.text,"html.parser")
# print(page)

# Afin d'éviter de moissoner l'information des entêtes de tableau, il faut créer une variable compteur. 

i = 0

# L'information que je cherche est dans un très gros tableau, il faut utiliser un Find all pour les réunir dans une liste. 
# On utilise ensuite une boucle pour consulter chacun des éléments de la liste. 
# Dans vos notes, chaque ligne de tableau est dans un élément HTML de type "tr".
# Je soupçonne que les éléments pertinents de mon tableau sont situés dans le "td"... je vais donc essayer les deux.

for ligne in page.find_all("tr"):
    
    # si i == 0 correspond à la première ligne (l'entête) et ne nous est donc pas utile. 
    if i > 0:
        # print(ligne)
        # À ce stade-ci, il n'y a absolument rien qui se passe. Mon workspace fait seulement se réimprimer.
        # J'ai également retenté le coup avec un autre URL... mais cela ne fonctionne toujours pas. 
        # Je vis le découragement. J'essaie avec vos trois scripts de moissonnage sans succès. 
        # i = 0, i > 0, ... rien n'y fait. 
        
        #Je comprends le concept d'aller chercher la partie de l'hyperlien vers la sous-page contenant plus d'infos sur le contrat.
        lien = ligne.a.get("href")
        # print(lien)
        
        # On doit recueillir cet hyperlien et le compléter.
        hyperlien = "http://www.pc.gc.ca/apps/pdc/" + lien
        # print(hyperlien)
        # Mon merveilleux programme ne fonctionne toujours pas, mais j'aimerais ne pas avoir zéro donc je tente de continuer.
        
        #Pour aller chercher les infos relatives au contrat (donc dans le lien à cliquer sur le site Internet)
        #Il faut répéter les étapes et définir de nouvelles variables quasi-identiques. 
        
        contenu2 = requests.get(hyperlien,headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")
        
        # Nous devons ensuite faire une liste vide dans laquelle seront enregistrées les infos relatives au contrat.
        contrat = []
        
        # Dans cette liste, il y aura d'abord l'hyperlien. 
        # Pour pouvoir retourner faire des vérifications plus tard. 
        contrat.append(hyperlien)
        
        # Le concept recommence. Chaque page de détails de contrat est aussi un petit tableau.
        # On va donc y chercher les éléments "tr/td" de chaque ligne, qu'on place dans une liste
        # par le biais de .find_all().
        # Il faut ensuite créer une autre boucle qui servira à aller chercher chacun des éléments du petit tableau.
        
        for item in page2.find_all("tr"):
            
            # Ceci est l'essai numéro 2 (à la manière d'un aparté pas clair)
            # avec le concept du script de moisson-environnement
            
            # Si l'on considère que chaque ligne "tr" contient deux "td"
            # A. La description de l'item B. L'item
            # Il faut donc créer une nouvelle variable dans laquelle sont déposés tous les "td"
            # que BS va trouver dans "item".
            
            # elements = item.find_all("td")
            # print(elements[1].text)
            # print("#"*50)
            # Retour à mon même problème où seul le maudit workspace s'écrit après un bref moment de réflexion.
            # Et cela, même si je tente de changer le tr pour des td et vice-versa.
            
            # Si cela fonctionnait, "element[0]" serait égal à "valeur du contrat"
            # et "element[1]" serait égal à, par exemple, "23 878,16$".
            
            # Considérant que c'est élément 1 que nous aimerions avoir dans notre csv
            # il faut l'ajouter à la liste contrat. 
            
            # contrat.append(elements[1].text)
        # print(contrat)
        
        # Ce merveilleux plan n'en était pas un. 
        # Dans le site de la défense, la balise était dans un "th"
        # Ce plan [environnement] était dans un "td"
        # Lorsque je print au début ma page, la valeur numérique de mon contrat est dans un vide
        # entre deux td... tr, td, th (JE SUIS PERDUE)
        # J'ai rééssayé de réécrire mon csv en le supprimant complètement mais il n'y a toujours pas de détails autre que l'URL desdits contrats.
            
            # ****** Reprise de l'essai numéro 1 ****** 
            # print(item)
            #Malgré mes efforts, cette marde ne fonctionne toujours pas. 
            #Si au moins elle avait la bonté d'âme de me dire dans quel zone se situe l'erreur.
            
            # L'explication selon laquelle des cellules vides pourraient faire planter le programme 
            # m'a redonné un brin d'espoir. 
            # Je vais tenter de mettre une condition faisant en sorte que les cellules vides 
            # mentionnent "none" dans notre liste alors que le "non néant" s'insère dans contrat. 
            
            if item.td is not None:
                contrat.append(item.td.text) 
                
                #Pour le néant (qui, je le prie, va régler mon bug)
            else:
                contrat.append(None)
            
        print(contrat)
        # Avec un sursaut d'étonnement, il ne se passe toujours rien d'autre que mon workspace qui se réimprime.
        
        # Si le tout fonctionnait bien, on ferait ici comme avec un API. 
        # Dans le meilleur des mondes, la liste contrat s'inscrirait dans une nouvelle ligne
        # d'un beau fichier CSV. 
        
        fin = open(fichier,"a")
        projet = csv.writer(fin)
        projet.writerow(contrat)
        
    # Il faut ensuite faire avancer le compteur pour que les autres tableaux soient également 
    # pris en considération.
    i =+ 1
    # DIANTRE IL SE PASSE QUELQUE CHOSE. Par miracle un CSV et des liens se sont enfin créés.
    # Par contre, il s'agit seulement des URL respectifs à chaque contrat 
    # alors que lorsque Magalie me montrait son script, tous les détails de ceux-ci y étaient également.
    
    # En conclusion, après avoir essayé deux plans, je comprends davantage comment faire un script de moissonnage.
    # Néanmoins, je n'ai pas du tout l'impression de détenir les codes, le jargon, nécessaire. 
    # Je n'arrive pas à comprendre vis-à-vis de quelle structure (de tableaux) je me trouve.
    # J'aurai pu réussir à trouver la faille dans mon script si j'avais compris en quoi le site de Parc canada 
    # était différent des deux (trois?) autres moissonnages que nous avons fait. 
    # J'ai vraiment mis beaucoup de temps à essayer de comprendre, mais je dois m'avouer vaincue.
    # Désolée de ne pas y être arrivée, j'aurais vraiment aimé... 
    # Je vous assure que nous adorons votre cours et que nous savons qu'il nous sera très utile.
    
    
