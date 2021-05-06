n = int(input())

while n < 1 or n > 9:
    print('Insira um número inicial entre 1 e 9')
    n = int(input())

m = int(input())

while m > 9 or m < 1:
    print('Insira um número final entre 1 e 9')
    m = int(input())

if n > m:
    print('Nenhuma tabuada nesse intervalo')
else:
    cont = n
    while cont <= m:
        for x in range (1,10):
            a = cont * x
            print('{} x {} = {}'.format(cont,x,a))
        cont = cont + 1
        print()
