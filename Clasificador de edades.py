#clasificador de edades y descuentos
edad=int(input("¿Que edad tienes?:"))
if edad <18:
    print("precio infantil")
elif edad >=18 and edad <=65:
    print (input("¿tiene carnet estudiantil:?"))
    if "si" :
        print("descuento de estudiante aplicado")
    if"no":
        print("precio adulto estandar")
else:
    print("precio de la tercera edad")
