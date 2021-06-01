###Créer une liste
>>>liste = [6,7,3,0]
[6,7,3,0]

###
>>>liste[2]
3

###Insert le chiffre 0 à l'index 2
>>>liste.insert(2,0)
[6,7,0,3,0]

###Insert le chiffre 8 à la
>>>liste.append(8)
[6,7,0,3,0,8]

###Concaténation pour ajouter au début
>>>liste = [9,7,8] + liste
[9,7,8,6,7,0,3,0,8]

###Classer par ordre croissant
>>>liste.sort()
[0,0,3,6,7,7,8,8,9]

###Enlever un élément 7
>>>liste.remove(7)
[0,0,3,6,7,8,8,9]