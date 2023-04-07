#Imprimir números pares
for i in range (0,21,2):
    print(i)
#Otra forma usando el operador módulo
for i in range (21):
    if i%2==0:
        print(i)
#Imprimir números impares entre 0 y 20
for i in range (21):
    if i%2==1:
        print(i)
#Otra forma de imprimir los impares
for i in range (21):
    if i%2 !=0:
        print(i)

#Acumulador
cont = 0
for i in range (6):
    cont= cont+1
    print(cont) 
#Números primos
num=int(input("Inserte un número: "))
cont= 0
for i in range(1, num+1):
    if num%i ==0:
        cont= cont+1
if cont==2:
    print("El número es primo")
else:
    print("El número no es primo")





    