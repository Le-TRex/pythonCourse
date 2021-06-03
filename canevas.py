import tkinter as tk

# Install tkinter : sudo apt-get install python3-pil.imagetk

fenetre = tk.Tk()

# label width et height en tailles de caractères ==> width=30 <=> largeur de 30 caractères
monlabel = tk.Label(fenetre, text="Nombre de clics : 0", width=30)
monlabel.grid(row=0, column=0)

label2 = tk.Label(fenetre, text="deuxième label")
label2.grid(row=0, column=1)

nombre_de_clics=0


def incremente_clics():
    global nombre_de_clics
    nombre_de_clics += 1
    monlabel.config(text="Nombre de clics : "+str(nombre_de_clics))


monbouton = tk.Button(fenetre, text="click me", command=incremente_clics) # increment_clics SANS parenthèses :
# command accepte un type fonction mais le but n'est PAS d'exécuter la fonction à la CRÉATION du bouton
# mais AU CLIC sur le bouton
monbouton.grid(row=1, column=0)


def raz_nombre_clics():
    global nombre_de_clics
    nombre_de_clics =0
    monlabel.config(text="Nombre de clics : " + str(nombre_de_clics))


bouton2 = tk.Button(fenetre, text="ràz nombre de clics", command=raz_nombre_clics)
bouton2.grid(row=1, column=1)

moncanevas=tk.Canvas(fenetre, width=400, height=300, background="blue")
moncanevas.grid(row=2, column=0, columnspan=2)

# ligne qui part de (x1, y1) à (x2, y2) /!\ les x vont de G à D mais les y vont de H en B
# donc démarrage à (0, 0) soit en haut à gauche, arrivée à droite en bas (400, 300)
ligne=moncanevas.create_line(0, 0, 400, 300, fill="white", width=50)
ligne2=moncanevas.create_line(400, 0, 0, 300, fill="white", width=50)

# /!\ coordonnées = point de départ H, point de départ V, point d'arrivée H point d'arrivée V
rectangle=moncanevas.create_rectangle(20, 40, 100, 100, fill="white")

ovale=moncanevas.create_oval(20, 40, 100, 100, fill="pink")

polygone=moncanevas.create_polygon(50, 150, 200, 50, 350, 150, 200, 250, fill="yellow")

ovale2=moncanevas.create_oval(150, 100, 250, 200, fill="blue")

moncanevas.create_text(200, 265, text="Ordem e progresso")

tk.mainloop()

# def fonction(a, b, c=0, **kwargs):
# c = paramètre optionnel
# **kwargs = key word arguments ==>
# fonction(6, 5, longueur=8) <== longueur = kwarg



