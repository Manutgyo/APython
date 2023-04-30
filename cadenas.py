nombre = input("Ingrese un nombre: ")
dato = input ("Ingrese un número entero: ")
try: 
   num = int (dato)
except:
   print("Dato no válido, no es un número entero") 
   quit()

for i in range (num):
   print(nombre)

palabra = input ("Ingrese una palabra o frase: ")
print(palabra[::-1])

   
   
