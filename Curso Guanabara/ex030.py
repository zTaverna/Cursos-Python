# PAR OU ÍMPAR

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))