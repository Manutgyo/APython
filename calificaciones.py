#Calificaciones automáticas
score = "Si"
while score == "Si":
    score = input("Ingrese su calificación: ")
    try:
        score = float(score)
        if score >= 0 and score <= 1:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >=0.7:
                print("C")
            elif score >=0.6:
                print("D")
            elif score < 0.6:
                print("F")
        else:
            print("Fuera de rango")
    except:
        print("Fuera de rango")
    score = input("Desea continuar (Si) (No): ")
