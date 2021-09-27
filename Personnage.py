class Personnage:

    def __init__(self,nom,prenom):
        self._nom = nom
        self._prenom = prenom

    def get_nom(self):
        return self._nom

    def set_nom(self, x):
        self._nom = x

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, x):
        self._prenom = x

    def __str__ (self):
        return 'Personnage(nom=' + self._nom + ' ,preonm=' + self._prenom + ')'
