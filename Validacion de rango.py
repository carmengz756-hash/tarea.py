#Pide al usuario un número entre 1 y 10. Si el número no está en ese rango, sigue pidiéndolo hasta que sea válido
numero=int(input("ingrese un numero entre 1 y 10:"))
while numero<1 and numero >10:
    print("numero fuera de rango.")
    breack
    numero=int(input("intenta denuevo:"))
print("numero valido:")
