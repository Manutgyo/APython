archivo = input("Ingrese un nombre archivo:")
try:
    texto = open(archivo)
except:
    print("El archivo no existe")
    quit()
palabrasordenadas = []
for linea in texto:
    linea = linea.rstrip()
    palabras = linea.split()
    #print(palabras)
    for x in palabras:
        if x in palabrasordenadas:
            continue
        palabrasordenadas.append(x)
        #print(palabras)
palabrasordenadas.sort()
print(palabrasordenadas)


