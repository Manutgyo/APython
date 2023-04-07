#Probando Try/Except
dato = "Si"
while dato == "Si":
    dato = input("Ingrese un número: ")
    try:
        num = int(dato)
    except:
        num = -1
    if num > 0:
        print("Buen trabajo")
    else:
        print("Esto no es un número")
    dato = input("Desea continuar (Si) (NO):")
