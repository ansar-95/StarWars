from Film import Film
from Personnage import Personnage
from Gentil import Gentil
from Mechant import Mechant
from Acteur import  Acteur
# Exercice 1 -a

film = Film("Star Wars épideode IV : Un nouvel espoir de George Lucas",1977,10000000,20000000,5)
film2 = Film("Star Wars épideode I : La menace fantôme de George Lucas",1999,10000000,20000000,5)

#Exercie 1 -b
"""
titre = input("Nom du film : \n")
annee = input("Année de sortie : \n")
numéroDepisode = input("Numéro depisode : \n")
cout = input("cout : \n")
recette = input("recette : \n")

film = Film(titre,int(annee),int(cout),int(recette),int(numéroDepisode))
print(film.__str__())
"""

#Exercice 3,4,5,6,7
"""
personnage = Personnage("i","v")
gentil = Gentil("heelo","worl",True)
mechant = Mechant("eee","fdfd",True)


liste = [personnage,gentil,mechant]

for i in liste:
    print(i)


"""

#Exercice 8

acteur = Acteur("bar","rer")
acteur2 = Acteur("ar","rer")
gentil = Gentil("heelo","worl",True)
mechant = Mechant("eee","fdfd",True)
mechant2 = Mechant("df","fdfd",True)
acteur.set_personnage(gentil)
acteur.set_personnage(mechant)
acteur.set_personnage(mechant2)
#print(acteur.nbPersonnages())
film.set_Acteurs(acteur)
film.set_Acteurs(acteur2)
print(film.nbPersonnages())
p= film.tri()
for i in p:
    print(i)

fiche = {film.get_annee():film, film2.get_annee():film2}
def makeBackUp(film:dict):
    for cle,valeur in film.items():
        p,f = valeur.calculBenefice()
        print(cle," - ",valeur.get_titre()," - ",p)

makeBackUp(fiche)
