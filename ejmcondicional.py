hrs = float(input("Ingrese el número de horas: "))
rate = float(input("Ingrese el pago por hora: "))
if hrs <= 40:
    pay = rate * hrs
    print(pay)
else: 
    over_hours = hrs - 40
    rate_overhours = (rate*1.5)*over_hours
    pay = (rate * 40) + rate_overhours
    print(pay)

#Función
hrs = float(input("Ingrese el número de horas: "))
rate = float(input("Ingrese el pago por hora: "))
def computepay(x,y):
    if hrs <= 40:
        pay = rate * hrs
        return pay
    else: 
        over_hours = hrs - 40
        rate_overhours = (rate*1.5)*over_hours
        pay = (rate * 40) + rate_overhours
        return pay
p = computepay(hrs,rate)
print("Pay", p)
