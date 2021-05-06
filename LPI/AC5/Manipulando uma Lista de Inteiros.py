inteiros = str(input()).strip().split(' ')

lista = []

comando = ''

for i in inteiros:
    x = int(i)
    lista.append(x)

while comando != 'final':
    comando = str(input())
    if comando.split(' ')[0] == 'inserir':
        numero = int(comando.split(' ')[1])
        lista.append(numero)
    elif comando.split(' ')[0] == 'remover':
        numero = int(comando.split(' ')[1])
        lista.remove(numero)
    elif comando.split(' ')[0] == 'parcial':
        print(' '.join(map(str, sorted(lista))))

print(' '.join(map(str, sorted(lista))))
