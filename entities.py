# -*- coding: utf-8 -*-
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)

class Joueur(db.Entity):
    id = PrimaryKey(int, auto=True)
    login = Required(unicode)
    email = Required(str)
    password = Required(unicode)
    ville = Optional("Ville")
    inventaire = Set("Objet")
    soif = Required(int, default=0)
    faim = Required(int, default=0)

    def check_password(self, password):
        return(password == self.password)

class Ville(db.Entity):
    id = PrimaryKey(int, auto=True)
    joueurs = Set(Joueur)
    banque = Set("Objet")

class Objet(db.Entity):
    id = PrimaryKey(int, auto=True)
    banque = Optional(Ville)
    inventaire = Optional(Joueur)
    def utiliser(joueur):
        print("Action non définie")

class Eau(Objet):
    def utiliser(joueur):
        if joueur.soif > 0:
            joueur.soif -= 1

class Nourriture(Objet):
    def utiliser(joueur):
        if joueur.faim > 0:
            joueur.faim -= 1
