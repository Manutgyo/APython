
def fah (x):
    f = (9/5)*x + 32
    print("La temperatura es:", f, "°F")
    return f

def kel (x):
     k = (x +273.15)
     print("La temperatura es:", k, "°K")
     return k

def ran (x):
    r = (x*(9/5)+491.67)
    print("La temperatura es:", r, "°R")
    return r
while True:
    dato= input("Ingrese temperatura en Celsius: ")
    peticion = input("Tipo de temperatura a calcular: Fahrenheit (F), Kelvin (K), Rankine (R), pasa finalizar (Terminar/fin): ")
    try: 
        numero = float(dato)
    except:
        print("Dato no válido")
        break
    if peticion == "Terminar" or peticion == "fin":
        break
    elif peticion == "F":
        fah (numero)

    elif peticion == "K":
        kel (numero)

    elif peticion == "R":
        ran (numero)
    else:
        print("Dato no válido")
quit()



