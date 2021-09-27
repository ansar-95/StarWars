from Personnage import Personnage
class Gentil(Personnage):

    def __init__(self,nom:str,prenom:str,force:bool):
        self._force = force
        self._personnage = Personnage(nom,prenom)

    def get_force(self):
        return self._force

    def set_force(self, x):
        self._force = x

    def get_personnage(self):
        return self._personnage

    def set_personnage(self, x):
        self._personnage = x


    def __str__ (self):
        return 'Gentil(force=' + str(self._force) + ')'
