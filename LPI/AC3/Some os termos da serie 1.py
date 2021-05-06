n = int(input())
soma = 1
x = 4
y = 5

for i in range(n - 1):
    soma += 1 / x
    x += y
    y += 2
print('{:.6f}'.format(soma))
    
