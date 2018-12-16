# coding=utf-8


class Origine:
    pass


class Humain(Origine):
    race = "Humain"
    EV = 30


class Barbare(Origine):
    race = "Barbare"
    EV = 35
    Competences = ["Ambidextrie", "Chercher des noises", "Sentir des Pieds", "Tête vide"]
    Competences_aux_choix = ["Armes de bourrin", "Bourre-pif", "Chevaucher", "Escalader",
                             "Intimider", "Nager", "Pister", "Tirer correctement"]


class Nain(Origine):
    race = "Nain"
    EV = 25
    competences = ["Appel du tonneau", "Instinct du trésor", "Pénible", "Radin"]
    competences_aux_choix = ["Appel des renforts", "Arnaque et carambouille", "Bourre-pif", "Bricolo du dimanche",
                             "Chercher des noises", "Fariboles", "Forgeron", "Méfiance", "Truc de mauviette",
                             "Tirer correctement (Hache de jet)"]


class Haut_Elfe(Origine):
    race = "Haut Elfe"
    EV = 25
    competences = ["Érudition", "Runes bizarres", "Tomber dans les pièges"]
    competences_aux_choix = ["Chef de groupe", "Chevaucher", "Jonglage et danse", "Nager", "Premiers soins",
                             "Tirer correctement"]


class Demi_Elfe(Origine):
    race = "Demi Elfe"
    EV = 28
    competences = ["Appel des renforts", "Détection", "Chouraver", "Méfiance"]
    competences_aux_choix = ["Bricolo du dimanche", "Chevaucher", "Érudition", "Escalader",
                             "Fouiller dans les poubelles", "Mendier et pleurnicher", "Nager", "Tirer correctement"]


class Elfe_Sylvain(Origine):
    race = "Elfe Sylvain"
    EV = 25
    competences = ["Chevaucher", "Naïveté touchante", "Premier soins", "Tirer correctement", "Tomber dans les pièges"]
    competences_aux_choix = ["Comprendre les animaux", "Déplacement silencieux", "Jonglage et danse", "Nager", "Pister",
                             "Tête vide"]


class Elfe_Noit(Origine):
    race = "Elfe Noir"
    EV = 25
    competences = ["Agoraphobie", "Déplacement silencieux", "Détection", "Tirer correctement"]
    competences_aux_choix = ["Ambidextrie", "Chouraver", "Érudition", "Escalader", "Forgeron", "Frapper lâchement",
                             "Méfiance", "Pister", "Runes bizzares"]


class Orque(Origine):
    race = "Orque"
    EV = 35
    competences = ["Agoraphobie", "Appel du sauvage", "Appel du tonneau", "Bourre-pif", "Instinct de survie",
                   "Sentir des pieds", "Tête vide"]
    competences_aux_choix = ["Armes de bourrin", "Chercher des noises", "Fouiller dans les poubelles",
                             "Truc de mauviette"]


class Demi_Orque(Origine):
    race = "Demi Orque"
    EV = 35
    competences = ["Agoraphobie", "Chercher des noises", "Instinct de survie", "Intimider", "Nager",
                   "Tirer correctement", "Truc de mauviette"]


class Gobelin(Origine):
    race = "Gobelin"
    EV = 20
    competence = ["Agoraphobie", "Appel des renforts", "Appel du sauvage", "Attire les monstres", "Instinct de survie",
                  "Instinct du trésor", "Senitr des pieds", "Tête vide"]
    competences_aux_choix = ["Bricolo du dimanche", "Désamorcer", "Escalader", "Forgeron"]


class Ogre(Origine):
    race = "Ogre"
    EV = 45
    competence=["Appel du ventre","Appel du tonneau","Armes de bourrin",""]


class Semi_Homme(Origine):
    race = "Semi Homme"
    EV = 25


class Gnome(Origine):
    race = "Gnôme des forêts du nord"
    EV = 15
