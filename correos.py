archivo = input("Ingrese nombre de archivo: ")
try:
    handler = open(archivo)
except:
    print("El archivo no existe")
    quit()
contador = dict()
dias = list()
correos = list()
bigcount = None
bigemail = None
for lineas in handler:
    lineas = lineas.rstrip()
    palabras = lineas.split()
    if len(palabras)<3 or palabras[0] != "From":
        continue
    #print(palabras)
    for x in palabras:
        correo = palabras[1]
        dia=palabras[2]
    #Es necesario separar el añadir los datos en la lista dentro del For, porque aparecerán datos repetidos
    dias.append(dia)
    correos.append(correo)
#for x in dias:
    #contador [x] = contador.get(x,0)+1

#El siguiente bucle asigna los datos de la lista al diccionario
for x in correos:
    contador [x] = contador.get(x,0)+1

#Identificando la clave con mayor número de items, al desactivar los días, solo se enfoca en los correos
for k,v in contador.items():
    if bigcount == None or v > bigcount:
        bigcount = v
        bigemail = k
print(bigemail, ":", bigcount)

print(contador)



