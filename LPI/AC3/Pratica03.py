num = float(input())
num = num*100

while num <= 70 or num >= 620 or num%10!=0:
    print('Preco invalido, refaca a leitura do pacote.')
    num = float(input())
    num = num*100
    


