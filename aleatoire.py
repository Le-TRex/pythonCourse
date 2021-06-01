import random

#range(10) => de 0 inclus à 9 inclus
#range(2,10) => de 2 inclus à 9 inclus

#produit des randoms entre 0 et 1
for i in range(10):
    print(random.random())

#produit des randoms entiers entre 0 inclus et 10 inclus
for i in range(10):
    print(random.randint(0, 10))
