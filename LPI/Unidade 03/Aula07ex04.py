numerador=-1
resposta=0

for denominador in range(1,51):
    numerador=numerador+2
    resposta=resposta+(numerador/denominador)

print(resposta)
