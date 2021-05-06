import math

x=float(input())
y=float

n1=x/(24*7)
valor1=math.ceil(n1)*91

n2=x/(5.4*7)
valor2=math.ceil(n2)*23

if x>168 :
    n3=x/(24*7)
    valor3=math.floor(n3)*91
    y=x-(168*math.floor(n3))
    n4=y/(5.4*7)
    valor4=math.ceil(n4)*23
    valor5=valor3+valor4
else :
    n3=0
    valor3=0
    n4=x/(5.4*7)
    valor4=math.ceil(n4)*23
    valor5=valor4
    

print("a)",math.ceil(n1),"lata(s) de 24 litros: R$ {:.2f}".format(valor1))
print("b)",math.ceil(n2),"lata(s) de 5.4 litros: R$ {:.2f}".format(valor2))
print("c)",math.floor(n3),"lata(s) de 24 litros e",math.ceil(n4),"lata(s) de 5.4 litros: R$ {:.2f}".format(valor5))
