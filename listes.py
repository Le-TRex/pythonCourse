# Créer et manipuler des listes

#Créer une liste :
liste = [6,7,3,0]
print(liste)
# ==> [6,7,3,0]

#----------------------------------------------------------------------------------------------------------------------#
#Afficher un élément de liste
print(liste[2])
# ==> 3

#----------------------------------------------------------------------------------------------------------------------#
#Inserer le chiffre 0 à l'index 2
liste.insert(2,0)
print(liste)
# => [6,7,0,3,0]

#----------------------------------------------------------------------------------------------------------------------#
#Inserer le chiffre 8 à la fin de la liste
liste.append(8)
print(liste)
# => [6,7,0,3,0,8]

#----------------------------------------------------------------------------------------------------------------------#
#Concaténation pour ajouter au début
liste = [9,7,8] + liste
print(liste)
# => [9,7,8,6,7,0,3,0,8]

#----------------------------------------------------------------------------------------------------------------------#
#Classer par ordre croissant
print(liste.sort())
# => [0,0,3,6,7,7,8,8,9]

#----------------------------------------------------------------------------------------------------------------------#
#Enlever un élément de valeur 7
print(liste.remove(7))
# => [0,0,3,6,7,8,8,9]

########################################################################################################################
#                                                  EXERCICES                                                           #
########################################################################################################################


# écrire un code qui rentre des nombres et intégrer ces valeurs dans un tableau
# liste=[] entree="" while entree!="stop": if entree.isdigit(): liste.append(int(entree))
# entree = input("Entrez un chiffre ") print(liste)

liste = []
entree = ""
while entree != "stop":
    if entree.isdigit():
        liste.append(int(entree))
    entree = input("Entre un nombre")
print(liste)

#calculer la moyenne des éléments de la list
#option1 :
somme = 0
for i in range(len(liste)):
    somme += liste[i]
print("moyenne: ", somme / len(liste))

#----------------------------------------------------------------------------------------------------------------------#
#option2 :
sum = 0
for element in liste:
    sum += element
print("average : ", sum/len(liste))

########################################################################################################################
import random

#Créer des listes de nombres aléatoires :
#option1 :
listOfNumbers = []
for i in range(10):
    listOfNumbers.append(random.randint(-5, 5))
print(listOfNumbers)

sum = 0
for element in listOfNumbers:
    sum += element
print("average of listOfNumbers : ", sum/len(listOfNumbers))

#----------------------------------------------------------------------------------------------------------------------#

#option2 :
secondListOfNumbers = [
    random.randint(-5, 5)
    for i in range(10)
]
print(secondListOfNumbers)

sum = 0
for element in secondListOfNumbers:
    sum += element
print("average of secondListOfNumbers : ", sum/len(secondListOfNumbers))

########################################################################################################################
import random

listOfNumbers = [
    random.randint(-100, 100)
    for i in range(20)
]
print(listOfNumbers)

#Trouver le plus grand nombre de la liste :
biggestNumber = listOfNumbers[0]

for element in listOfNumbers:
    if element > biggestNumber:
        biggestNumber = element
print(biggestNumber)

########################################################################################################################