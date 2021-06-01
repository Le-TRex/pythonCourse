# écrire un code qui rentre des nombres et intégrer ces valeurs dans un tableau
# liste=[] entree="" while entree!="stop": if entree.isdigit(): liste.append(int(entree))
# entree = input("Entrez un chiffre ") print(liste)

liste=[]
entree=""
while entree!="stop":
    if entree.isdigit():
        liste.append(int(entree))
    entree=input("Entre un nombre")
print (liste)

#calculer la moyenne des éléments de la liste
