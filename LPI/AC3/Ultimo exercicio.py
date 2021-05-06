n = int(input())
soma = -1
den = 2

for x in range(n - 1):
    if den % 2 == 0:
        soma += 1 / den
    else:
        soma -= 1 / den
    den += 1
print('{:.6f}'.format(soma))
