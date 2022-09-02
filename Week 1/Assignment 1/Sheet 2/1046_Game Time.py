a,b = map(int, input().split())

if b>a:
    print("O JOGO DUROU {} HORA(S)".format(b-a))
else:
    print("O JOGO DUROU {} HORA(S)".format(24-a+b))