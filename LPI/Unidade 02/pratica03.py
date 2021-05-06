import math
n1 = float(input())

if n1>=100:
    print(math.floor(n1/100), 'nota(s) de R$ 100.00')
    n1= n1 - (math.floor(n1/100)*100)
    if n1>=50:
        print(math.floor(n1/50), 'nota(s) de R$ 50.00')
        n1= n1 - (math.floor(n1/50)*50)
        if n1>=20:
            print(math.floor(n1/20), 'nota(s) de R$ 20.00')
            n1= n1 - (math.floor(n1/20)*20)
            if n1>=10:
                print(math.floor(n1/10), 'nota(s) de R$ 10.00')
                n1= n1 - (math.floor(n1/10)*10)
                if n1>=5:
                    print(math.floor(n1/5), 'nota(s) de R$ 5.00')
                    n1= n1 - (math.floor(n1/10)*10)
                    if n1>=2:
                        print(math.floor(n1/2), 'nota(s) de R$ 2.00')
                        n1= n1 - (math.floor(n1/2)*2)
    elif n1>=20:
            print(math.floor(n1/20), 'nota(s) de R$ 20.00')
            n1= n1 - (math.floor(n1/20)*20)
            if n1>=10:
                print(math.floor(n1/10), 'nota(s) de R$ 10.00')
                n1= n1 - (math.floor(n1/10)*10)
                if n1>=5:
                    print(math.floor(n1/5), 'nota(s) de R$ 5.00')
                    n1= n1 - (math.floor(n1/10)*10)
                    if n1>=2:
                        print(math.floor(n1/2), 'nota(s) de R$ 2.00')
                        n1= n1 - (math.floor(n1/2)*2)
