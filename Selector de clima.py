#el selector del clima
clima=input("¿como esta el clima hoy?:").lower()
print("Soleado","Lluvioso","Nevado","Nublado")
match clima:
    case"soleado":
        print("usa ropa lijera")
    case"lluvioso":
        print("cuidado al conducir")
    case"nevado":
        print("lleve ropa abrigadora")
    case"nublado":
        print("esta corriendo viento")
