a,b,c = map(float, input().split())

lst = [a,b,c]

lst.sort(reverse=True)

if lst[0] >= lst[1]+lst[2]:
    print("NAO FORMA TRIANGULO")
elif lst[0]*lst[0] == lst[1]*lst[1]+lst[2]*lst[2]:
    print("TRIANGULO RETANGULO")
elif lst[0]*lst[0] > lst[1]*lst[1]+lst[2]*lst[2]:
    print("TRIANGULO OBTUSANGULO")
elif lst[0]*lst[0] < lst[1]*lst[1]+lst[2]*lst[2]:
    print("TRIANGULO ACUTANGULO")
if lst[0]==lst[1]==lst[2]:
    print("TRIANGULO EQUILATERO")
elif lst[0]==lst[1] or lst[1]==lst[2]:
    print("TRIANGULO ISOSCELES")