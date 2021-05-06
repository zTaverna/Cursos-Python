item = ''
itens = []
maior_item = ''
maior = ''

while item != '0 0 0':
    item = input()
    itens.append(item)

for x in itens:
    compra = x.split(' ')
    total = int(compra[1])*float(compra[2])
    if maior_item == '':
        maior_item = x + ' ' + str(total)
    else:
        maior = maior_item.split(' ')
        if float(maior[3]) < total:
            maior_item = x + ' ' + str(total)


maior_split = maior_item.split(' ')

if maior_split[0] == '0':
    print('nao tem compras')
else:
    print('Item mais caro')
    print('Codigo: {}'.format(maior_split[0]))
    print('Quantidade: {}'.format(maior_split[1]))
    print('Custo: {:.2f}'.format(round(float(maior_split[3]),2)))
