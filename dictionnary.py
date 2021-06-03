dictionnary = {
    "key1": "value1",
    "key2": "value2",
    "key3": 3,
    "key4": 6
}
# Affiche la valeur associée à la clé "key4"
print(dictionnary["key4"])
print("")

# Modifie la valeur associée à la clé "key4"
dictionnary["key4"] = "pouet"
print(dictionnary["key4"])
print("")

# Ajoute un couple au dictionnaire
dictionnary["key5"] = "troubadour"
print(dictionnary)
print("")

# Affiche tout le dictionnnaire
print(dictionnary)
print("")

# Affiche les clés du dictionnaire
for i in dictionnary:
    print(i)
print("")

# Affiche la liste des tuples
for i in dictionnary.items():
    print(i)
print("")

# Affiche la liste des couples clé-valeur
for i in dictionnary.items():
    print("clé:", i[0], ", valeur:", i[1])
print("")

# Affiche la liste des couples clé-valeur
for key, value in dictionnary.items():
    print("clé:", key, ", valeur :", value)

# Sauvegarder un dictionnaire dans un fichier texte dans lequel il y aura un couple clé-valeur par ligne.
# la clé et la valeur seront séparés par un ";"

with open("dictionnaire.txt", "w") as my_file:
    for key, value in dictionnary.items():
        my_file.write(str(key) + " ; " + str(value) + "\n")


def sauvegarde_dictionnaire(dictionnaire, nom_fichier, separateur=" "):
    with open(nom_fichier, "w") as fichier:
        for cle, valeur in dictionnaire.items():
            fichier.write(str(cle)+separateur+str(valeur)+"\n")


sauvegarde_dictionnaire(dictionnary, "dico2.txt")
