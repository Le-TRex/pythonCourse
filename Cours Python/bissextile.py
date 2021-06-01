#test année bissextile
# bissextile si divisible par 4
# sauf si divisible par 100
# sauf celles divisibles par 400 qui sont bissextiles

# annee=input("Entre une année: ")
# if not annee.isdigit():
#     print("Année non reconnue")
# else:
#     annee=int(annee)
#     if annee%4==0:
#         if annee%100==0:
#             if annee%400==0:
#                 print("C'est une année bissextile")
#             else:
#                 print("Ce n'est pas une année bissextile")
#         else:
#             print("C'est une année bissextile")
#     else:
#         print("Ce n'est pas une année bissextile")
#     exit()



##### VERSION AMELIOREE AVEC LE WHILE
entree = ""
while entree!="stop":
    if entree.isdigit():
        annee=int(entree)
        if annee%400==0:
            print("Bissextile")
        elif annee%100==0:
            print("Non Bissextile")
        elif annee%4==0:
            print("Bissextile")
        else:
            print("Non Bissextile")
    entree = input("Entrez une année: ")







