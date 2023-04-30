conteo = 0
suma = 0
promedio = 0
file = input("Inserte nombre de archivo: ")
documento = open(file)
for linea in documento:
    if linea.startswith("X-DSPAM-Confidence:"):
        conteo = conteo +1
        inicio = linea.find(":")
        numero = linea [inicio+1:]
        numero = float(numero)
        suma = suma + numero
    else:
        continue

if conteo > 0:
    promedio = suma / conteo
    print("Promedio spam confidence:",promedio)
else: 
    print("No se pudo calcular un promedio")

