# Créer une fonction :
# def nomDeMaFonction(paramètre):
#     instructions

def absoluteValue(number):
    if number > 0:
        return number
    else:
        return -number


print(absoluteValue(-6))
print(absoluteValue(12))


def isASuepriorToB(a, b):
    return a > b


print(isASuepriorToB(2, 5))
print(isASuepriorToB(5, 2))


def returnFirstElementofAList(listToEvaluate):
    return listToEvaluate[0]


print(returnFirstElementofAList([2, 5, 6]))


def biggestNumberOfAList(listToEvaluate):
    if not listToEvaluate:
        return None
    biggestNumber = listToEvaluate[0]
    for element in listToEvaluate:
        if element > biggestNumber:
            biggestNumber = element
    return biggestNumber


print(biggestNumberOfAList([8, 3, 9, 5]))
print(biggestNumberOfAList([-4, -1, -1, -3]))
print(biggestNumberOfAList([]))
print(biggestNumberOfAList([100]))

myList = [8, 5, 4, 9, 7]


def swap(listToEvaluate, i, j):
    auxilary = listToEvaluate[i]
    listToEvaluate[i] = listToEvaluate[j]
    listToEvaluate[j] = auxilary


swap(myList, 1, 3)
print(myList)


def is_palindrome(list_to_evaluate):
    if len(list_to_evaluate) < 1:
        return None
    for i in range(len(list_to_evaluate)//2): # // ==> inverse du modulo cf dessous
        if list_to_evaluate[i] != list_to_evaluate[-i-1]: # xxx[-i-1] ==> cf dessous
            return False
    return True

# division euclidienne (avec reste) :
# 15 / 2 ==> 15 = 2 * 7 + 1
# avec 15 ==> Dividende, 2 ==> diviseur, 7 ==> quotient et 1 ==> reste
# avec modulo on veut le reste :
# 15 % 2 ==> 1 car 15/2 = 2 * 7 + 1
# avec division euclidienne (aka division entière) on veut le quotient
# 15 //2 ==> 7 car 15/2 = 2 * 7 + 1

# xxx[-i-1] ==> dans une boucle for i in range(len(list)):
# print(list[-i-1]) permet d'afficher les élements du dernier au premier alors que :
# print(list[i]) permet d'afficher du premier au dernier

my_list = ["a", "b", "c", "d"]
for i in range(len(my_list)):
    print(my_list[-i-1])

#inverse la liste
print(my_list[::-1])

print("palindrome1")
print(is_palindrome([]))
print(is_palindrome("cocoococ"))
print(is_palindrome("pouet"))
print(is_palindrome([1, 2, 3, 4, 4, 3, 2, 1]))
print(is_palindrome([1, 3, 7, 9, 5, 4]))
print(is_palindrome([8, 2, 8]))

def is_palindrome_2(list_to_evaluate):
    return list_to_evaluate == list_to_evaluate[::-1]

print("palindrome2")
print(is_palindrome_2([]))
print(is_palindrome_2("cocoococ"))
print(is_palindrome_2("pouet"))
print(is_palindrome_2([1, 2, 3, 4, 4, 3, 2, 1]))
print(is_palindrome_2([1, 3, 7, 9, 5, 4]))
print(is_palindrome_2([8, 2, 8]))


# Fonction qui prend en paramètre une liste et qui renvoie le minimum et l'indice du minimum
# Jeu du juste prix