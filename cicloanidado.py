#Números primos del 1-100
for i in range (1,101):
    cont=0
    for j in range (1,i+1):
        if i%j == 0:
            cont+=1
    if cont == 2:
        print(i)
#El contador se pone en 2, porque cuando se consigue que se divida únicamente 2 veces, es primo, solo se divide: 1. Por sí mismo 2. Por otro número


