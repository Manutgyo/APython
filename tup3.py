archivo = input("Ingrese un nombre de archivo: ")
try: 
    handle =open(archivo)
except:
    print("Archivo inválido")
    quit()
contador = dict()
palabras = list()
lista = list()
for lineas in handle:
    lineas=lineas.rstrip()
    word = lineas.split()
    for x in word:
        palabras.append(x)
palabras = "".join(palabras)
palabras = palabras.lower()
for x in palabras:
    #método.isalpha() evalúa que solo haya letras
    if not x.isalpha():
        continue
    contador[x]= contador.get(x,0)+1
    datos = contador.items()
for k,v in datos:
    lista.append((v,k))
lista = sorted(lista,reverse=True)
for v,k in lista[:5]:
    print(k,v)





        






