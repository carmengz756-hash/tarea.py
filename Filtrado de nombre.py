#Filtrado de nombres: Dada una lista de nombres ["Ana", "Pedro", "Alberto","Maria"],usa un for e if para imprimir solo los nombres que comienzan con la letra ´A´
nombres={"Ana","Pedro","Alberto","Maria"}
for nombre in nombres:
    if nombre.startswith("A"):
        print(nombre)
