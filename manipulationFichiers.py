fichier = open("blabla.txt", "w") # ("nomFichier", "mode") avec mode => r=read, w=write, a=append
fichier.write("blabla\n")
fichier.close()

# le bloc with permet de gérer la fermetur propre du fichier donc pas besoin de ficher.close()
with open("blabla.txt", "a") as fichier:
    fichier.write("blublu\n")
    fichier.write("blibli\n")

with open("blabla.txt", "r") as fichier:
    texte = fichier.read() # read() en mode "brut"
    print("1ère lecture :\n" + texte)
    texte = fichier.read()
    print("2ème lecture:\n" + texte) # rien car tête de lecture en fin de fichier
    fichier.seek(0) # placcer tête de lecture au début
    texte = fichier.read()
    print("3ème lecture:\n" + texte)

    # texte = texte.split("\n") # permet de spliter là ou se trouve le caractère choisi (ici \n) et génère une liste ==> ['blabla', 'blublu', '']

    # texte = fichier.readlines() # permet une lecture ligne par ligne ==> ['blabla\n', 'blublu\n']
    # print(texte)

########################################################################################################################

# Écrire 10 nombres aléatoires dans un fichier (1/ligne)
# Ouvrir le fichier en lecture et calculer la somme

import random

with open("numbers.txt", "w") as my_file:
    for i in range(10):
        my_file.write(str(random.randint(0, 10))+"\n")

with open("numbers.txt", "r") as my_file_content:
    content = my_file_content.readlines()
    # content = content.split()

print(content)
sum_of_numbers = 0
for i in range(len(content)):
    sum_of_numbers += int(content[i])
print(sum_of_numbers)
