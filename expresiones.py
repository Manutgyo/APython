import re
archivo = input("Ingrese el nombre del archivo: ")
try:
    han = open(archivo)
except:
    print("Archivo no válido")
    quit()
datos = list()
for linea in han:
    linea = linea.rstrip()
    ext = re.findall("^New Revision: .*?([0-9]+)", linea)
    if len(ext) > 0:
        ext = int(ext[0])
        datos.append(ext)
adicion = sum(datos)
conteo = len(datos)
promedio= adicion / conteo
print(promedio)



