import math
p1 = float(input())
p2 = float(input())
p3 = float(input())
f = float(input())
m = float
f = f*100
m = (p1*2 + p2*2 + p3*3)/7
print('Frequencia: {:.0f}%'.format(f))
print('Media: {:.1f}'.format(m))
if f<75:
    print('Aluno reprovado por faltas!')
elif m>9:
    print('Aluno aprovado com louvor!')
elif m>=6 and m<=9:
    print('Aluno aprovado!')
elif m>=3.9 and m<6:
    print('Aluno de recuperação!')
else:
    print('Aluno reprovado!')
