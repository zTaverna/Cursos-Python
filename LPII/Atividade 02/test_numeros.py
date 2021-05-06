import numeros

lista_teste_numeros = [2, 3, 6, 10, 24, 25, 28, 59, 153, 1634]

for n in lista_teste_numeros:
    print(n, numeros.eh_primo(n))

primos = numeros.lista_primos(100)

print('lista de primos: ', primos)

for n in lista_teste_numeros:
    print(n, numeros.eh_armstrong(n))

armstrongs = numeros.lista_armstrong(1000)

print('lista de armstrongs: ', armstrongs)

for n in lista_teste_numeros:
    print(n, numeros.eh_perfeito(n))

perfeitos = numeros.lista_perfeitos(10000)

print('lista de perfeitos: ', perfeitos)