x = int(input())
y = x
n = int(input())
z = 0
cont = 0

while z < n:
    cont = cont + 1
    z = y * cont

print('O numero',x,'tem',cont-1,'multiplos menores que {}.'.format(n))

