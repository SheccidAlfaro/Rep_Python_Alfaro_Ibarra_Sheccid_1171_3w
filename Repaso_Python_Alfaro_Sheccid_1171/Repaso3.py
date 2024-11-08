print("")
print("Alfaro_Ibarra_Sheccid_1171_Repaso_Python")
print("")
#Declarar variables, en este caso se declaran dos variables para apellido y nombre
nm="SheccidA"
ap="Alfaro"
#Se pregunta al usuario por su nombre
us=str(input("Ingrese su nombre: "))
print("")
#A partir de if, se comprueba si el nombre ingresado es igual a "Sheccid" 
if us== nm:
    print("Bienvenido ", us)
else:
    print("Lo siento, usuario desconocido.")
print("")
#Se pregunta al usuario por su apellido
us1=str(input("Ingrese su Apellido: "))
print("")
#A partir de if, se comprueba si el apellido ingresado es igual a "Alfaro"
if us1==ap:
    print("Bienvenido ", us1, " ", us)
else:
    print("Lo siento, usuario desconocido.")