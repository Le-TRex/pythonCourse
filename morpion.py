import tkinter as tk

# Install tkinter : sudo apt-get install python3-pil.imagetk

window = tk.Tk()

square_size = 100
margin = 10
my_size = 3 * square_size
total_number_of_squares = 9
list_of_squares = ["vide" for i in range(total_number_of_squares)]
print(list_of_squares)
# représente l'état de la partie à un instant donné.
# "vide" : Case Vide
# "x" : Case avec une croix,
# "o" : Case avec un rond
move = 0

my_canvas = tk.Canvas(window, width=my_size, height=my_size, background="pink")
my_canvas.grid(row=0, column=0)

my_canvas.create_line(0, square_size, my_size, square_size)
my_canvas.create_line(0, 2 * square_size, my_size, 2 * square_size)
my_canvas.create_line(square_size, 0, square_size, my_size)
my_canvas.create_line(2 * square_size, 0, 2 * square_size, my_size)

my_label = tk.Label(window, text="Au tour des croix")
my_label.grid(row=1, column=0)


def square(x, y):
    # Version courte :
    return 3 * (y//square_size) + x//square_size
    # Version longuette
    # if x < square_size:
    #     if y < square_size:
    #         return 0
    #     elif y < 2*square_size:
    #         return 3
    #     else:
    #         return 6
    # elif x < 2 * square_size:
    #     if y < square_size:
    #         return 1
    #     elif y < 2*square_size:
    #         return 4
    #     else:
    #         return 7
    # else:
    #     if y < square_size:
    #         return 2
    #     elif y < 2*square_size:
    #         return 5
    #     else:
    #         return 8


def draw_cross(square):
    x = (square % 3) * square_size
    y = (square // 3) * square_size
    my_canvas.create_line(x + margin, y + margin, x + square_size - margin, y + square_size - margin, fill="MediumVioletRed", width=3)
    my_canvas.create_line(x + margin, y + square_size - margin, x + square_size - margin, y + margin, fill="MediumVioletRed", width=3)


def draw_circle(square):
    x = (square % 3) * square_size
    y = (square // 3) * square_size
    my_canvas.create_oval(x + margin, y + margin, x + square_size - margin, y + square_size - margin, outline="purple", width=3)



def is_victorious(square):
    line = square // 3
    column = square % 3
    # Alignement horizontal
    if list_of_squares[3 * line] == list_of_squares[3 * line + 1] == list_of_squares[3 * line + 2]:
        return True
    # Alignement vertical
    if list_of_squares[column] == list_of_squares[column + 3] == list_of_squares[column + 6]:
        return True
    # Alignement diagonal
    if line == column and list_of_squares[0] == list_of_squares[4] == list_of_squares[8]:
        return True
    if line == 2 - column and list_of_squares[2] == list_of_squares[4] == list_of_squares[6]:
        return True
    return False


def on_click(event):
    global move
    x = event.x
    y = event.y

    square_number = square(x, y)

    # Écrire les coordonnées du pixel sur lequel on clique :
    # my_canvas.create_text(x, y, text=str(x) + "," + str(y))
    # Écrire le numéro de la case dans laquelle on a cliqué :
    # my_canvas.create_text(x, y, text=str(square(x, y)))

    if list_of_squares[square_number] == "vide":
        if move % 2 == 0:
            # Tracer une croix dans la case
            draw_cross(square(x, y))
            list_of_squares[square_number] = "x"
            if is_victorious(square_number):
                my_label.config(text="Victoire des Croix !")
                my_canvas.unbind("<Button-1>")
            else:
                my_label.config(text="Au tour des Ronds")
        else:
            # Tracer un cercle dans la case
            draw_circle(square(x, y))
            list_of_squares[square_number] = "o"
            if is_victorious(square_number):
                my_label.config(text="Victoire des Ronds !")
                my_canvas.unbind("<Button-1>")
            else:
                my_label.config(text="Au tour des Croix")
        move += 1


# Button-1 = clic gauche
my_canvas.bind("<Button-1>", on_click)

tk.mainloop()
