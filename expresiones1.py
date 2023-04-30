archivo = input("Ingrese nombre del archivo: ")
try:
    han = open(archivo)
except:
    print("Archivo no válido")
    quit()
import re
datos = list()
for linea in han:
    linea = linea.rstrip()
    dato = re.findall("[0-9]+",linea)
    if len(dato)> 0:
        for i in range(len(dato)):
            num = int(dato[i])
            datos.append(num)
print(datos)
adicion = sum(datos)
print(adicion)
