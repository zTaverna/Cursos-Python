salario = float(input())
desconto = 0
if salario<=1751.81:
    desconto=0.08*salario
    print('Desconto do INSS: R$ {:.2f}'.format(desconto))
elif salario>1751.81 and salario<=2919.72:
    desconto=0.09*salario
    print('Desconto do INSS: R$ {:.2f}'.format(desconto))
elif salario>2919.72 and salario<=5839.45:
    desconto=0.11*salario
    print('Desconto do INSS: R$ {:.2f}'.format(desconto))
else:
    desconto=5839.45*0.11
    print('Desconto do INSS: R$ {:.2f}'.format(desconto))
    
