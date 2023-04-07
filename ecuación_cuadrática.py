import math
repetir="S"
while repetir =="S" or repetir=="s":
    a=float(input("Ingrese el coeficiente a: "))
    b=float(input("Ingrese el coeficiente b: "))
    c=float(input("Ingrese el coeficiente c: "))
    #Cálculo del discriminante
    discriminante =b**2-4*a*c
    if discriminante > 0:
        r1= (-b+math.sqrt(discriminante))/(2*a)
        r2= (-b-math.sqrt(discriminante))/(2*a)
        print("Los puntos de corte en el eje X son:", r1, r2)
    else:
        base= -b/2*a
        print("Raíz 1:", base, "+", (math.sqrt(-discriminante))/(2*a), "i")
        print("Raíz 2:", base, "-", (math.sqrt(-discriminante))/(2*a), "i")
    #While con cierre, asegurar que siempre tenga un fin
    repetir=input("¿Desea continuar? S/s: ")


