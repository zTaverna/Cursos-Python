from random import randint
from time import sleep

# JOGO DE ADIVINHAÇÃO

computador = randint(1, 5) # faz o computador randomizar os números
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input("Em que número eu pensei? ")) # jogador tenta adivinhar
print('Processando...')
sleep(2)
while jogador > 5 or jogador <= 0:
    jogador = int(input('Digite um número válido: '))

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('PERDEU! Eu pensei no número {} e não no {}!'.format(computador, jogador))
