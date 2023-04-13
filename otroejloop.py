largest = None
smallest = None
while True: 
    dato = input("Ingrese un número: ")
    if dato == "done":
        break
    try:
        numero = int(dato)
        if largest == None and smallest == None:
            largest = numero
            smallest = numero
        elif numero > largest:
            largest = numero
        elif numero < smallest:
            smallest = numero
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)


