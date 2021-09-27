class Acteur:

    def __init__(self,nom:str,prenom:str):
        self._nom = nom
        self._prenom = prenom
        self._objPersonnage = list()

    def get_nom(self):
        return self._nom

    def set_nom(self, x):
        self._nom = x

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, x):
        self._prenom = x

    def get_personnage(self):
        return self._objPersonnage

    def set_personnage(self, x):
        self._objPersonnage.append(x)

    def nbPersonnages(self):
        return len(self._objPersonnage)

    def __repr__(self):
        return repr((self._nom, self._prenom, self._objPersonnage))

    def __str__ (self):
        return 'Acteur(nom=' + self._nom + ' ,preonm=' + self._prenom + ')'

