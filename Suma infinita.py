#La Suma Infinita: Pide al usuario que ingrese cuántos números desea sumar. Luego, usa un for para solicitar esos numeros,sumalos y muestra el total
suma=0
cantidad=int(input("¿cuantos numeros desea sumar?:"))
print(cantidad)
for x in range(cantidad):
    numero=float(input(f"ingrese el numero {x+1}:"))
    suma+=numero
print("la suma total es:",suma)
