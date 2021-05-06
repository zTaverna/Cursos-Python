s = str(input())

def contagem(s):
    caracteres = 0
    for x in s:
        caracteres += 1
    return caracteres

print(contagem(s))
