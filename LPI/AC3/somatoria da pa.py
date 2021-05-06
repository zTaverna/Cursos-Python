r = int(input())
n = int(input())
soma = 0

for c in range(1, n+1, r):
    soma = soma + c

print('A somatoria da PA eh:',soma)
