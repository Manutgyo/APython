#Versión corta
name = input("Enter file:")
handle = open(name)
conteo= dict()
for lines in handle:
    if not lines.startswith("From "): continue
    palabras=lines.split()
    Tmp= palabras[5]
    Horas= Tmp.split(":")
    Hor= Horas[0]
    conteo[Hor]=conteo.get(Hor, 0)+1
for k,v in sorted(conteo.items()):
    print(k, v)


#Versión larga 
archivo= input("Ingrese nombre de archivo: ")
try:
    handle= open(archivo)
except:
    print("Archivo inválido")
    quit()
contador = dict()
horas_exactas = list()
horas = list()
tiempo = list()
temp = list()
for linea in handle:
    linea = linea.rstrip()
    palabras = linea.split()
    if len(palabras)<3 or palabras[0]!= "From":
        continue
    for palabra in palabras:
        hora = palabras [5]
    horas_exactas.append(hora)

for x in horas_exactas:
    horas= x.split(":")
    for t in horas:
        hora = horas[0]
    tiempo.append(hora)
for x in tiempo:
    contador[x]= contador.get(x,0)+1
#print(contador)
for k,v in contador.items():
    temp.append((k,v))
temp= sorted(temp)
for k,v in temp:
    print(k,v)


    
