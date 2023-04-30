archivo = input("Ingrese nombre de archivo: ")
try:
    handle = open(archivo)
except:
    print("Archivo no encontrado")
    quit()
contador = dict()
correos = list()
tmp = list()
for linea in handle:
    linea = linea.rstrip()
    palabras = linea.split()
    if len(palabras)<3 or palabras[0]!="From":
        continue
    for palabra in palabras:
        correo = palabras[1]
    correos.append(correo)
#print(len(correos), correos)
for x in correos:
    contador[x]= contador.get(x,0)+1
for k,v in contador.items():
    tmp.append((v,k))
tmp= sorted(tmp, reverse=True)
for v,k in tmp[0:1]:
    print(k,v)



