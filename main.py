# main.py : programme principal de la playlist de party

# TODO 0 : corriger les erreurs de syntaxe dans le fichier playlist

# TODO 1 : importer le module playlist
from playlist import *

# TODO 2 : créer le dictionnaire vide ma_playlist
#          et les listes titres et durees (5 éléments chacune)
ma_playlist = {}
titres = ['Mal luné', 'Halo', 'Macarena', 'Daddy chocolat', 'Gris']
durees = [120, 330, 177, 220, 199]


# TODO 3 : avec une boucle for et range(len(titres)),
#          ajouter chaque chanson à ma_playlist, en utilisant le module
for i in range(len(titres)):
    ajouter_chanson(ma_playlist,titres[i],durees[i])


# TODO 4 : afficher chaque chanson avec sa durée formatée
#          (ex. : Nuit blanche - 3:05)
for key, value in ma_playlist.items():
    print(f"{key} - {formater_duree(value):>5}")



# TODO 5 : afficher la durée totale de la playlist, formatée
total = duree_totale(ma_playlist)
print("Durée totale -", formater_duree(total))


# TODO 6 : afficher la chanson la plus longue
print("Chanson la plus longues:", chanson_la_plus_longue(ma_playlist))

# TODO 7 : demander une durée maximale en secondes (input, converti en int),
#          puis afficher la liste des chansons plus courtes que cette durée
duree_max = int(input("Entrez une durée maximal : "))
liste_chansons_courtes = chansons_courtes(ma_playlist, duree_max)
print(liste_chansons_courtes)


# TODO 8 : demander le titre d'une chanson à retirer
#          - si elle est absente : afficher un message
#          - sinon : la retirer et réafficher la playlist
retirer = input("Entrez le titre à retirer : ")
if retirer not in ma_playlist:
    print("Ce titre est absent dans la playlist")
else:
    ma_playlist = retirer_chanson(ma_playlist, retirer)
    print(ma_playlist)
# TODO 9 : tester votre programme, corriger les erreurs d'exécutions et de logique
#          incluant celles dans le module.

# TODO 10 : tester avec des valeurs incorrectes, exemple un titre qui n'existe pas,
#           une durée en str, et ajouter la gestion d'exceptions, incluant dans le module.