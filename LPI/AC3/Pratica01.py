import math
semana = []
var = 0

while len(semana) < 7:
    dia = int(input())
    semana.append(dia)
    if dia >= 100:
        var += 1
media = sum(semana) / 7
print(var)
print("{0:.0f}".format(media))

    
