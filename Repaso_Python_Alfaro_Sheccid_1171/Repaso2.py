print("")
print("Alfaro_Ibarra_Sheccid_1171_Repaso_Python")
print("")
#Preguntar al usuario su calificacion
nta=int(input("Ingrese la calificacion:"))
#Utilizar un condicional para determinar si la calificacion es mayor o igual dependiendo de la calificacion ingresada
if nta<=5:
    print("Suspenso")

if nta ==6:
    print("Suficiente")

if nta==7:
    print("Bien")

if nta==8 and nta==9:
    print("Notable")

if nta==10:
    print("Sobresaliente")

if nta >10:
    print("Nota invalida")