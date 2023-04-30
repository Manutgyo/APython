conteo = 0
file = input("Inserte un nombre de archivo: ")
if file == "na na boo boo":
    print("NA NA BOO BOO PARA TI -  Te he atrapado")
    quit()
try:
    documento = open(file)
except:
    print("El arhivo no puede ser abierto:", file)
    quit()
for linea in documento:
    #La siguiente línea imprime todo el documento en mayúsculas línea por línea
    #print(linea.upper()) 
    conteo = conteo + 1
print("Hay", conteo, "líneas en",file)




