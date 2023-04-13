conteo= 0
suma= 0
promedio= 0
while True:
    linea = input("Ingrese un número: ")
    if linea == "Fin" or linea == "fin":
        break 
    try:
        numero = float(linea)
        conteo = conteo+1
        suma = suma+numero
        promedio = suma/conteo
    except: 
        print("dato erróneo")
print(suma, conteo, promedio)

    

        