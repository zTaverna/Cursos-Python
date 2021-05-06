# RADAR ELETRÔNICO

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('-=-' * 20)
    print('Multado! Você excedeu o limite que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('-=-' * 20)
print('Tenha um bom dia! Dirija com segurança!')