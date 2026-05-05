#Adivina el Número: Crea una variable secreto = 7 . Pide al usuario que adivine el número. Dale pistas si es más alto o más bajo, y usa un bucle para que intente hasta acertar
secreto=7

while True:
    b=int(input("Adivine el numero:"))
    if b>secreto:
        print("es un numero mas bajo")
    elif b<secreto:
        print("es un numero mas alto")
        continue
    else:
        print("correcto!")
        break
