anos = str(input()).split(' ')

def contaDigitos (digito):
    return digito >= 1000

def ehBissexto (digito):
    return digito % 4 == 0 and digito % 100 != 0 or digito % 400 == 0

def Mensagem (ano):
    if contaDigitos (ano):
        if ehBissexto (ano):
            if ano >= 2020:
                print('O ano {} serah bissexto'.format(ano))
            else:
                print('O ano {} foi bissexto'.format(ano))
        else:
            print('O ano {} NAO eh bissexto'.format(ano))
    else:
        print('Ano invalido')

for i in anos:
    x = int(i)
    Mensagem(x)
