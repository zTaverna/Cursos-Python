def encontrarMultiplus(n,m):
    i = 0
    multiplus = []
    while i <= n:
        if i % m == 0:
            multiplus.append(i)
            i = i + 1
        else:
            i = i + 1
    return multiplus

numero1 = int(input())
numero2 = int(input())

multiplus = encontrarMultiplus(numero1,numero2)

print('Os multiplus de',numero2,'são: ',multiplus) 
