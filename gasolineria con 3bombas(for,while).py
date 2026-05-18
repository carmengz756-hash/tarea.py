#Instrucciones: Crea un sistema para una gasolinera que tiene 3 bombas de carga

Bomba=[1,2,3]
for x in range(1,4):
   Bomba=input("desea cragar combustible?: ")
   if Bomba=="no":
      continue
    
   while Bomba =="si" :
        monto=float(input("ingrese el monto: "))
        if monto <=0:
             monto=float(input("error,ingrese monto valido: "))
             print("Bomba x cargada con {monto}")
             break
