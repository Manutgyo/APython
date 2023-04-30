import random
l = list()
for i in range(11):
    num = round(random.random()*5,1)
    l.append(num)
cal = l.copy()
for i in range(len(l)):
    if l[i]> 4.5:
        cal [i] = "E"
    elif l [i] < 4.5 and l [i] >= 4:
        cal [i] = "B"
    elif l[i] < 4 and l [i]>= 3.5:
        cal [i] = "A"
    elif l [i] < 3.5 and l[i] >= 3:
        cal [i] = "R"
    elif l [i] < 3 and l[i] >= 2.5:
        cal [i] = "D"
    elif l [i] < 2.5 and l[i] >= 2:
        cal [i] = "D"
    elif l [i] < 2 and l[i] >= 0:
        cal [i] = "I"
print(l)
print(cal)