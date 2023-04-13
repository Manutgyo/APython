#Encontrar el dato más grande
largest_so_far= None
numbers = [3,41,12,9,74,15]
for the_num in numbers:
    if largest_so_far == None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far= the_num
    print(largest_so_far, the_num)
print("El número más grande es:", largest_so_far)

#Contar 
conteo = 0
for i in numbers:
    conteo= conteo + 1
    print(conteo, i)

#Sumar
suma = 0
for i in numbers:
    suma = suma +i
print("Total:", suma)

#Promedio
N= 0
sum = 0
for i in numbers:
    N = N+1
    sum = sum + i
promedio = sum/N
print(promedio)
