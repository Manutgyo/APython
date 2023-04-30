archivo= input("Ingrese el nombre del archivo:")
try:
    texto = open(archivo)
except:
    print("No se puede leer el archivo")
    quit()
contador = 0
for linea in texto:
    linea = linea.rstrip()
    if not linea.startswith("From:"):
        continue
    contador = contador +1 
    palabras = linea.split()
    print(palabras[1])
print("Hay", contador, "líneas en el archivo que inician con la palabra From al inicio")

enteros = []
while True:
    pregunta = input("Ingrese un número: ")
    if pregunta == "fin" or pregunta == "done" or pregunta== "Fin":
        break
    try:
        numero = int(pregunta)
    except:
        print("No es un número")
        quit()
    enteros.append(numero)
print("Máximo:", max(enteros))
print("Mínimo:", min(enteros))

    
