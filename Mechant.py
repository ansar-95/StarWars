from Personnage import Personnage
class Mechant(Personnage):

    def __init__(self,nom:str,prenom:str,coteObcure:bool):
        self._coteObcure = coteObcure
        self._personnage = Personnage(nom,prenom)

    def get_force(self):
        return self._coteObcure

    def set_force(self, x):
        self._coteObcure = x

    def get_personnage(self):
        return self._personnage

    def set_personnage(self, x):
        self._personnage = x


    def __str__ (self):
        return 'Mechant(coteObcure' + str(self._coteObcure) + ')'
