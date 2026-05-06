#Calculadora de Pares: Pide números al usuario. Si el número es par, imprímelo; si  es impar, usa continue para ignorarlo. El bucle termina cuando el usuario escriba 0
numero=int(input("ingrese numeros:"))
while numero %2==0:
    print("es un numero par")
    break
else:
    numero=int(input("ingrese otro numero, 0 para salir:"))
print("programa finalizado")
