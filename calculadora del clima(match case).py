#Calculadore de clima
clima=input("Ingrese estacion actual:").lower()
print("primavera","verano","otoño","invierno")
match clima:
    case"primavera":
        print("usa ropa lijera")
    case"verano":
        print("usa ropa comoda")
    case"otoño":
        print("esta corriendo viento")
    case"invierno":
        print("abrigese")
    case:
        print("error")
