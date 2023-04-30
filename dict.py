archivo = input("Ingrese nombre de archivo: ")
try:
    handler = open(archivo)
except:
    print("No existe el archivo")
    quit()
claves = dict()
for lines in handler:
    lines = lines.rstrip()
    lines = lines.split()
    for word in lines:
        claves[word]= claves.get(word, 0)+ 1
#print(claves.keys())

while True:
    palabra = input("¿Qué palabra quieres revisar?")
    if palabra == "done" or palabra =="fin"or palabra=="Fin":
        break
    if palabra in claves:
        print("Si está")
    else:
        print("No está")

