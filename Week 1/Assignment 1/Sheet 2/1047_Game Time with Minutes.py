a,b,c,d = map(int, input().split())

if c>a and d>=b:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(c-a,d-b))
elif c>a and b>d:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(c-a-1,60-(b-d)))
elif a>c and d>=b:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-a+c,d-b))
elif a>c and b>d:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-a+c-1,60-(b-d)))
elif a==c and d>b:
    print("O JOGO DUROU 0 HORA(S) E {} MINUTO(S)".format(d-b))
elif a==c and d<b:
    print("O JOGO DUROU 23 HORA(S) E {} MINUTO(S)".format(60-(b-d)))
elif a==b==c==d:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")