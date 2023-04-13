#Definir una función
def suma (a,b):
    adicion = a+b
    return adicion
print(suma(2,5))

#Usar librería random
import random
for i in range (10):
    datos = random.randint(1,10)
    print (datos)

#Probando Choice
tup = (1,2,3)
m = random.choice(tup)
print("Escojo", m)



