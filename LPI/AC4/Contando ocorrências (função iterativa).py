q = 0

n = str(input())
m = str(input())

a = list(n)

for i in a:
    if i == m:
        q += 1
if q == 0:
    print('Caractere nao encontrado.')
else:
    print('O caractere buscado ocorre {} vezes na sequencia.'.format(q))
