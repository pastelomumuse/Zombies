#!/usr/bin/env python2

#Importer les classes du fichier enties.py (Ville, Joueur...)
from entities import *

# Verrouiller temporiarement l'accès à la base de données
# pour éviter les conflits (durant l'exécution des lignes indentées)
with db_session:
    # Créé une instance de la classe Ville, et la stocke dans la variable v1
    # Passage de paramètre nommé au constructeur Ville pour définir immédiatement
    # le nom de la ville
    v1 = Ville(nom='Springfield')

    v2 = Ville(nom='Marseille')

    # Création d'un joueur, même topo
    j1 = Joueur(login='pastel', email='pastelomumuse@linuxw.info', password='azerty')
    j2 = Joueur(login='twix', email='thegame@perdu.lost', password='azertyuiop')

    # Pour accéder aux attributs d'un objet (Joueur, Ville...), il faut utiliser le point  '.'
    print(j1.login)

    # On peut changer le login :
    j1.login = "noob"

    # Attribution de la Ville v1 en tant qu'attribut 'ville' du Joueur j1
    j1.ville = v1

    # Utilisation de la méthode checkpassword de la classe Joueur (ou objet j1)
    # pour valider un mot de passe
    if j1.check_password("azerty"):
        print("mot de passe correct")
    else:
        print("mot de passe incorrect")

    # Pour sauvegarder les modifications dans la base de données
    db.flush()
