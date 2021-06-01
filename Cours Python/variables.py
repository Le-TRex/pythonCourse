# L'indentation compte!




###### Va demander le prénom et afficher quand il aura reçu le input
# prenom=input("Dis ton nom !")
# age=input("T'as quel âge toi !")
# print("Bonjour",prenom,", tu as",str(age),"ans.")

########OPERATIONS SUR LES VARIABLES
# prenom=input("Dis ton nom !")
# annee=input("Tu es de quelle année?")
#####Il faut utiliser la fonction int pour que l'input soit considéré comme un integer
# age = 2021 - int(annee)
# print("Bonjour",prenom,", tu es de",annee,"? Alors tu vas avoir",age,"ans cette année.")

# ###### CONDITIONS
# age=int(input("Quel âge as-tu?"))
# ### correspond à :
# ##age=input("Quel âge as-tu?")
# ##age=int(age)
# if age<18:
#     print("Tu es mineur")
#     print("Tu ne peux pas rentrer sur le site")
# elif age>30:
#     print("Vous êtes pas tout neuf vous!")
#     print("Mais bienvenue quand même!!!")
# else:
#     print("Tu es majeur")
#     print("Bienvenue à toi!")
# print("Fin de programme.")



prenom=input("Dis ton nom !")
age=int(input("Quel âge as-tu?"))
if prenom=="Thibaut" and age==32:
    print("Tu es une personne formidable")
else:
    print("Mais t'es carrément mieux que Thibaut!")


