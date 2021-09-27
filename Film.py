class Film:


    def __init__(self,titre:str,annee:int,cout:int,recette:int,numeroDepisode):
        self._titre = titre
        self._annee = annee
        self._cout = cout
        self._recette = recette
        self._numeroDepisode = numeroDepisode
        self._acteurs =list()

    def get_titre(self):
        return self._titre

    def set_titre(self, x):
        self._titre = x

    def get_annee(self):
        return self._annee

    def set_annee(self, x):
        self._annee = x

    def get_NumeroDepisode(self):
        return self._numeroDepisode

    def set_NumeroDepisode(self, x):
        self._numeroDepisode = x

    def get_Cout(self):
        return self._cout

    def set_Cout(self, x):
        self._cout = x

    def get_Recette(self):
        return self._recette

    def set_Recette(self, x):
        self._recette = x

    def get_Acteurs(self):
        return self._acteurs

    def set_Acteurs(self, x):
        self._acteurs.append(x)

    def nbActeurs(self):
        return len(self._acteurs)

    def nbPersonnages(self):
        somme = 0
        for i in self._acteurs:
            somme += i.nbPersonnages()

        return somme
    def calculBenefice(self):
        if self._recette - self._cout > 0:
            return self._recette - self._cout, True
        else:
            return self._recette - self._cout, False

    def isBefore(self,annee):
        if self._annee < annee:
            return True
        else:
            return False
    def tri(self):
        return sorted(self._acteurs, key=lambda acteurs: acteurs._nom)

    def __str__(self):
        return 'Film(titre=' + self._titre + ' ,annee=' + str(self._annee) + ' , cout='+ str(self._cout)+' ,recette='+str(self._recette)+' , numero D episode='+str(self._numeroDepisode)+')'



