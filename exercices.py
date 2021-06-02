# Jeu du juste prix

import random
# import randint from random
number_to_guess = random.randint(1, 100)
# number_to_guess = randint(1, 100)
number_of_trials = 0
chosen_number = 0
play_again = ""

while play_again != "stop":
    print("Devinez le nombre mystère ! ")
    while chosen_number != number_to_guess:
        number_of_trials += 1
        print("Essai numéro :", number_of_trials)
        chosen_number = int(input("Devinez le nombre mystère (entre 1 et 100)"))
        while chosen_number < 1 or chosen_number > 100:
            print("Le nombre saisi n'est pas compris entre 0 et 100")
            chosen_number = int(input("Devinez le nombre mystère (entre 1 et 100)"))
        if chosen_number > number_to_guess:
            print("le nombre à deviner est plus petit")
        elif chosen_number < number_to_guess:
            print("Le nombre à deviner est plus grand")
    else:
        print("Bravo ! Vous avez trouvé en :", number_of_trials, "essais !")
        play_again = input("Nouvelle partie ? tapez 'stop' pour sortir du jeu")
else:
    print("Ok ! Ciao bobye !")


# Fonction qui prend en paramètre une liste et qui renvoie la valeur du minimum et l'indice du minimum
# Tuple : ensemble d'éléments au nombre fixe

# def function():
#     return 0, 1, 8
#
#
# a, b, c = function()
#
# print(a)
# print(b)
# print(c)


def smallest_number_and_index(list_to_evaluate):
    if not list_to_evaluate:
        return None
    smallest_number = list_to_evaluate[0]
    index_of_smallest_number = 0
    for i in range(len(list_to_evaluate)):
        if list_to_evaluate[i] < smallest_number:
            smallest_number = list_to_evaluate[i]
            index_of_smallest_number = i
    return index_of_smallest_number, smallest_number


# print(smallest_number_and_index([8, 3, 9, 5]))
# print(smallest_number_and_index([-4, -1, -1, -3]))
# print(smallest_number_and_index([]))
# print(smallest_number_and_index([100]))
#
#
# mini, index = smallest_number_and_index([-4, -1, -1, -3])
#
# print("valeur min :", mini)
# print("index:", index)


def swap(listToEvaluate, i, j):
    auxilary = listToEvaluate[i]
    listToEvaluate[i] = listToEvaluate[j]
    listToEvaluate[j] = auxilary


# swap(myList, 1, 3)
# print(myList)

list_to_sort=[8, 4, 0, 6, 1, 5, 7, 2]


def sort_selection(list_to_be_sorted):
    for i in range(len(list_to_be_sorted)):
        index, value = smallest_number_and_index(list_to_be_sorted[i:])
        swap(list_to_be_sorted, index + i, i)
        print(list_to_be_sorted)

    # index, value = smallest_number_and_index(list_to_be_sorted)
    # swap(list_to_be_sorted, index, 0)
    #
    # index, value = smallest_number_and_index(list_to_be_sorted[1:])
    # swap(list_to_be_sorted, index + 1, 1)
    #
    # index, value = smallest_number_and_index(list_to_be_sorted[2:])
    # swap(list_to_be_sorted, index + 2, 2)

print(list_to_sort)
sort_selection(list_to_sort)
print(list_to_sort)
