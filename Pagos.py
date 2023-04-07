#Programa que determina el valor a pagar al empleado después de los descuentos de ley
base = int(input ("Ingrese su salario base: "))
hora_extra= int(input("Ingrese las horas extras trabajadas en el mes sin puntos o comas: "))
bonificaciones = int(input("¿Recibió bonificaciones? SI= 1 ; NO= 0: "))
if bonificaciones == 1:
    pago_bono= base*0.05
else:
    pago_bono= 0
valor_hora = base/192
pago_hoextra = (float(hora_extra))*(valor_hora*1.25)
salario_parcial= pago_hoextra+base+pago_bono
#print(salario_parcial, pago_bono)
salud = salario_parcial*0.035
pension = salario_parcial*0.04
caja_comp = salario_parcial*0.01
salario_neto= salario_parcial-salud-pension-caja_comp
print(salario_neto)

