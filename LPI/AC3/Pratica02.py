cpeso = 0
cdimensao = 0
cfinal=0
peso = float(input())

while peso <= 0:
    print('Peso invalido!')
    peso = float(input())

if peso > 0:
    print('Peso valido!')

altura = float(input())
largura = float(input())
comprimento = float(input())

while altura <= 0 or largura <= 0 or comprimento <=0:
    print('Dimensoes invalidas!')
    altura = float(input())
    largura = float(input())
    comprimento = float(input())

if altura > 0 or largura > 0 or comprimento > 0:
    print('Dimensoes validas!')

if peso > 500 or altura > 28 or largura > 28 or comprimento > 28 or (altura + largura + comprimento) > 52:
    print('Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo!')
else:
    if peso <= 100:
        cpeso = 0.50
    else:
        cpeso = 0.50 + (peso - 100)//10/10
    if (altura+largura+comprimento) <= 22:
        cdimensao = 0.20
    else:
        cdimensao = 0.20 + ((altura+largura+comprimento)-22)//2/10
    cfinal = cpeso + cdimensao
    print("Custo total do envio: R$ {:.2f}".format(cfinal))
