import math

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def get_longueur(self):
        return self.longueur

    def get_largeur(self):
        return self.largeur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def set_largeur(self, largeur):
        self.largeur = largeur


class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)
        # Rectangle.__init__(self, cote, cote) ==> autre méthode, fonctionnelle elle aussi

    def __del__(self):
        print("destructeur de la classe Rectangle")

    def set_largeur(self, largeur):
        self.largeur = largeur
        self.longueur = largeur

    def set_longueur(self, longueur):
        self.largeur = longueur
        self.longueur = longueur


class Circle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.diametre = 2 * self.rayon

    def __del__(self):
        print("destructeur de la classe Circle")

    def perimetre(self):
        return self.diametre * math.pi

    def set_longueur(self, longueur):
        self.longueur = longueur

    def set_rayon(self, rayon):
        self.rayon = rayon
        self.diametre = 2 * self.rayon

    def get_rayon(self):
        return self.rayon

    def rapport_perimetre_sur_diametre():
        return math.pi


my_rectangle = Rectangle(5, 3)

print(type(my_rectangle))
print(my_rectangle.aire())
print(my_rectangle.perimetre())

my_second_rectangle = Rectangle(8, 3)
print(my_second_rectangle.aire())
print(my_second_rectangle.perimetre())

my_circle = Circle(5)
print(my_circle.perimetre())
print(Circle.rapport_perimetre_sur_diametre())
del my_circle

my_square = Carre(5)
print(my_square.perimetre())