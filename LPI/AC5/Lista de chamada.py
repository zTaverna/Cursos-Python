inteiros = str(input()).strip().split(' ')

lista = []
nomes = []

for i in inteiros:
    x = int(i)
    lista.append(x)

if lista[0] > 1 and lista[1] <= lista[0] and lista[0] <= 20:
    for j in range(0,lista[0]):
        name = str(input())
        nomes.append(name)

    nomes.sort()

    n = lista[1] - 1
    print(nomes[n])
else:
    print('Valor inválido')
