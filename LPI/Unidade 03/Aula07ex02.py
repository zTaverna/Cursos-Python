n = int(input('Inserir numero para gerar a sequência de Fibonnaci :'))

u_1 = 1
u_2 = 1
count = 0

lista = [0,1,1]

for vic in range(0, n):
    count = u_1 + u_2
    u_1 = count
    u_2 = (count - u_2)
    lista.append(count)

print(lista)
